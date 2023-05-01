from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

from task_manager.utils import AuthorizationCheck
from task_manager.tasks.models import Task

from .models import Status
from .forms import StatusForm


class StatusesView(AuthorizationCheck, ListView):
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


class StatusCreateView(AuthorizationCheck, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = 'statuses/form.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')
    extra_context = {
        'title': _('Create status'),
        'button': _('Create'),
    }


class StatusUpdateView(AuthorizationCheck, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/form.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status is successfully updated')
    extra_context = {
        'title': _('Update status'),
        'button': _('Update'),
    }


class StatusDeleteView(AuthorizationCheck, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')
    extra_context = {
        'title': _('Delete status'),
        'text': _('Are you sure you want to delete '),
        'button': _('Yes, delete'),
    }

    def post(self, request, *args, **kwargs):
        label_id = kwargs['pk']
        tasks_with_label = Task.objects.filter(labels=label_id)

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            if not tasks_with_label:
                return self.form_valid(form)
            messages.error(
                self.request,
                _('It is not possible to delete a status because it is in use')
            )
            # ru: "Невозможно удалить статус, потому что он используется"
            return redirect('labels')
        else:
            return self.form_invalid(form)
