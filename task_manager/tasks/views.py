from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from task_manager.tasks.filters import TaskFilter
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from task_manager.users.models import User
from task_manager.utils import AuthorizationCheck, TaskPermissions

from .models import Task
from .forms import TaskForm


class TasksView(AuthorizationCheck, FilterView):
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    template_name = 'tasks/tasks.html'
    extra_context = {
        'title': _('Tasks'),                                        # ru: "Задачи"
        'fields': ['ID', _('Name'), _('Status'), _('Author'),       # ru: "Имя", "Статус", "Автор"
                   _('Executor'), _('Created at'), ''],            # ru: "Исполнитель", "Дата создания"
        'create_btn': _('Create task'),                             # ru: "Создать"
        'edit_btn': _('Edit'),                                      # ru: "Изменить"
        'delete_btn': _('Delete'),                                  # ru: "Удалить"
        'filter_btn': _('Show'),                                    # ru: "Показать"
    }


class TaskView(AuthorizationCheck, DetailView):
    model = Task
    template_name = 'tasks/task.html'
    extra_context = {
        'title': _('Task preview'),                                 # ru: "Просмотр задачи"
        'fields': ['ID', _('Name'), _('Status'), _('Author'),
                   _('Executor'), _('Created at'), ''],
        'edit_btn': _('Edit'),
        'delete_btn': _('Delete'),
    }


class TaskCreateView(AuthorizationCheck, SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')        # ru: "Задача успешно создана"
    extra_context = {
        'title': _('Create task'),                          # ru: "Создать задачу"
        'button': _('Create'),                              # ru: "Создать"
    }

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(AuthorizationCheck, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task is successfully updated')     # ru: "Задача успешно изменена"
    extra_context = {
        'title': _('Update task'),                          # ru: "Изменение задачи"
        'button': _('Update'),                              # ru: "Изменить"
    }


class TaskDeleteView(TaskPermissions, AuthorizationCheck, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')        # ru: "Задача успешно удалена"
    extra_context = {
        'title': _('Delete task'),                          # ru: "Удаление задачи"
        'text': _('Are you sure you want to delete '),      # ru: "Вы уверены, что хотите удалить "
        'button': _('Yes, delete'),                         # ru: "Да, удалить"
    }
