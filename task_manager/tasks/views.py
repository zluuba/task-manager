from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from django_filters.views import FilterView

from task_manager.utils import AuthorizationCheck, TaskPermissions
from task_manager.tasks.filters import TaskFilter
from task_manager.users.models import User

from .forms import TaskForm
from .models import Task


class TasksView(AuthorizationCheck, FilterView):
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    template_name = 'tasks/tasks.html'
    extra_context = {
        'title': _('Tasks'),
        'fields': ['ID', _('Name'), _('Status'), _('Author'),
                   _('Executor'), _('Created at'), ''],
        'create_btn': _('Create task'),
        'edit_btn': _('Edit'),
        'delete_btn': _('Delete'),
        'filter_btn': _('Show'),
    }


class TaskView(AuthorizationCheck, DetailView):
    model = Task
    template_name = 'tasks/task.html'
    extra_context = {
        'title': _('Task preview'),
        'fields': ['ID', _('Name'), _('Status'), _('Author'),
                   _('Executor'), _('Created at'), ''],
        'edit_btn': _('Edit'),
        'delete_btn': _('Delete'),
    }


class TaskCreateView(AuthorizationCheck, SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = 'form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')
    extra_context = {
        'title': _('Create task'),
        'button': _('Create'),
    }

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(AuthorizationCheck, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task is successfully updated')
    extra_context = {
        'title': _('Update task'),
        'button': _('Update'),
    }


class TaskDeleteView(
    AuthorizationCheck, TaskPermissions,
    SuccessMessageMixin, DeleteView
):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')
    extra_context = {
        'title': _('Delete task'),
        'text': _('Are you sure you want to delete '),
        'button': _('Yes, delete'),
    }
