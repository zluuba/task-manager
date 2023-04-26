from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from .models import Status
from .forms import StatusForm


class StatusesView(ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/statuses.html'
    extra_context = {
        'title': _('Statuses'),
        'fields': ['ID', _('Name'), _('Created at'), ''],
        'create_btn': _('Create status'),
        'edit_btn': _('Edit'),
        'delete_btn': _('Delete'),
    }


class StatusCreateView(CreateView):
    form_class = StatusForm
    template_name = 'statuses/form.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')      # ru: "Статус успешно создан"
    extra_context = {
        'title': _('Create status'),                        # ru: "Создать статус"
        'button': _('Create'),                              # ru: "Создать"
    }


class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/form.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status is successfully updated')   # ru: "Статус успешно изменён"
    extra_context = {
        'title': _('Update status'),                        # ru: "Изменить статус"
        'button': _('Update'),                              # ru: "Изменить"
    }


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')      # ru: "Статус успешно удалён"
    extra_context = {
        'title': _('Delete status'),                        # ru: "Удаление статуса"
        'text': _('Are you sure you want to delete '),      # ru: "Вы уверены, что хотите удалить "
        'button': _('Yes, delete'),                         # ru: "Да, удалить"
    }
