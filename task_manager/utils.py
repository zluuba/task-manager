from django.utils.translation import gettext as _
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

from task_manager.users.models import User
from task_manager.tasks.models import Task

from django.http import Http404


class AuthorizationCheck(LoginRequiredMixin):
    """
    Checks permissions to the pages.
    If user isn't logged in, redirects to the login page.
    """

    login_url = reverse_lazy('login')
    permission_denied_message = _('You are not logged in! Please log in.')
    redirect_field_name = None

    def get_login_url(self):
        messages.error(self.request, self.permission_denied_message)
        return str(self.login_url)


class UserPermissions(UserPassesTestMixin):
    """
    Checks updating / deleting (user profile) permissions.
    If the selected user is not the current user,
    user will not be updating / deleting.
    """

    def test_func(self):
        current_user = self.request.user.id
        chosen_user = self.kwargs['pk']

        if current_user != chosen_user:
            return False
        return True

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            messages.error(self.request,
                           _('You have no rights to change another user.'))
            return redirect(reverse_lazy('users'))
        return super().handle_no_permission()


class TaskPermissions(UserPassesTestMixin):
    """
    Checks permissions to task deleting.
    If the user is not the author of the task, task will not be deleted.
    """

    def test_func(self):
        current_user = self.request.user.id
        task_id = self.kwargs['pk']

        try:
            task_author = Task.objects.get(pk=task_id).author.pk
        except (Task.DoesNotExist, User.DoesNotExist):
            raise Http404

        if current_user != task_author:
            return False
        return True

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            messages.error(self.request,
                           _('The task can be deleted only by its author'))
            return redirect(reverse_lazy('tasks'))
        return super().handle_no_permission()
