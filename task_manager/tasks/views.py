from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from django_filters.views import FilterView

from task_manager.utils import AuthorizationCheckMixin, TaskPermissionsMixin
from task_manager.tasks.filters import TaskFilter

from .forms import TaskForm
from .models import Task


class TaskView(AuthorizationCheckMixin, DetailView):
    model = Task
    template_name = 'tasks/task.html'


class TasksView(AuthorizationCheckMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    template_name = 'tasks/tasks.html'


class TaskCreateView(AuthorizationCheckMixin,
                     SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        current_user = self.request.user.user
        form.instance.author = current_user
        return super().form_valid(form)


class TaskUpdateView(AuthorizationCheckMixin,
                     SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully updated')


class TaskDeleteView(AuthorizationCheckMixin, TaskPermissionsMixin,
                     SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')
