from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

from task_manager.utils import AuthorizationCheck
from task_manager.tasks.models import Task

from .models import Label
from .forms import LabelForm


class LabelsView(AuthorizationCheck, ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'labels/labels.html'
    extra_context = {
        'title': _('Labels'),
        'fields': ['ID', _('Name'), _('Created at'), ''],
        'create_btn': _('Create label'),
        'edit_btn': _('Edit'),
        'delete_btn': _('Delete'),
    }


class LabelCreateView(AuthorizationCheck, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = 'labels/form.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created')      # ru: "Метка успешно создана"
    extra_context = {
        'title': _('Create label'),                        # ru: "Создать метку"
        'button': _('Create'),                              # ru: "Создать"
    }


class LabelUpdateView(AuthorizationCheck, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/form.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label is successfully updated')   # ru: "Метка успешно изменена"
    extra_context = {
        'title': _('Update label'),                        # ru: "Изменить метку"
        'button': _('Update'),                              # ru: "Изменить"
    }


class LabelDeleteView(AuthorizationCheck, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')      # ru: "Метка успешно удалена"
    extra_context = {
        'title': _('Delete label'),                        # ru: "Удаление метки"
        'text': _('Are you sure you want to delete '),      # ru: "Вы уверены, что хотите удалить "
        'button': _('Yes, delete'),                         # ru: "Да, удалить"
    }

    def post(self, request, *args, **kwargs):
        label_id = kwargs['pk']
        tasks_with_label = Task.objects.filter(labels=label_id)

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            if not tasks_with_label:
                return self.form_valid(form)
            messages.error(self.request, 'It is not possible to delete a label because it is in use')
            # ru: "Невозможно удалить метку, потому что она используется"
            return redirect('labels')
        else:
            return self.form_invalid(form)
