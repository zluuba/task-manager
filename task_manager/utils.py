from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.contrib import messages

from django.http import Http404

from task_manager.tasks.models import Task
from task_manager.users.models import User


class AuthorizationCheck(LoginRequiredMixin):
    """
    Checks permissions to the pages.
    If user isn't logged in, redirects to the login page.
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please log in.')
            )
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class UserPermissions:
    """
    Checks updating / deleting (user acc) permissions.
    If the selected user is not the current user,
    user will not be updating / deleting.
    """

    def dispatch(self, request, *args, **kwargs):
        current_user = request.user.id
        chosen_user_id = kwargs['pk']

        if current_user != chosen_user_id:
            messages.error(
                request, _('You have no rights to change another user.')
            )
            return redirect('users')

        return super().dispatch(request, *args, **kwargs)


class TaskPermissions:
    """
    Checks permissions to task deleting.
    If the user is not the author of the task, task will not be deleted.
    """

    def dispatch(self, request, *args, **kwargs):
        try:
            task_author = str(Task.objects.get(pk=kwargs['pk']).author)
            curr_user = str(
                User.objects.get(username=request.user).get_fullname()
            )

            if curr_user != task_author:
                messages.error(
                    request, _('The task can be deleted only by its author')
                )
                return redirect('tasks')
            return super().dispatch(request, *args, **kwargs)

        except (Task.DoesNotExist, User.DoesNotExist):
            return super().dispatch(request, *args, **kwargs)
