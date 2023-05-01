from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages

from task_manager.tasks.models import Task


class AuthorizationCheck(LoginRequiredMixin):
    """
    Checks permissions to the pages.
    If user isn't logged in, redirects to the login page.
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You are not logged in! Please log in.')
            # ru: "Вы не авторизованы! Пожалуйста, выполните вход."
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
            messages.error(request, 'You have no rights to change another user.')
            # ru: "У вас нет прав для изменения другого пользователя."
            return redirect('users')

        return super().dispatch(request, *args, **kwargs)


class TaskPermissions:
    """
    Checks permissions to task deleting.
    If the user is not the author of the task, task will not be deleted.
    """

    def dispatch(self, request, *args, **kwargs):
        task_author = str(Task.objects.get(pk=kwargs['pk']).author)
        curr_user = str(request.user)

        if curr_user != task_author:
            messages.error(request, 'The task can be deleted only by its author')
            # ru: "Задачу может удалить только её автор"
            return redirect('tasks')

        return super().dispatch(request, *args, **kwargs)
