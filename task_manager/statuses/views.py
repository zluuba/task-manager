from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.urls import reverse_lazy

from task_manager.utils import AuthorizationCheckMixin
from task_manager.tasks.models import Task

from .models import Status
from .forms import StatusForm


class StatusesView(AuthorizationCheckMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/statuses.html'


class StatusCreateView(AuthorizationCheckMixin,
                       SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')


class StatusUpdateView(AuthorizationCheckMixin,
                       SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully updated')


class StatusDeleteView(AuthorizationCheckMixin,
                       SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')

    def post(self, request, *args, **kwargs):
        status_id = kwargs['pk']
        tasks_with_status = Task.objects.filter(status=status_id)

        if tasks_with_status:
            messages.error(
                self.request,
                _('It is not possible to delete a status '
                  'because it is in use')
            )
            return redirect('statuses')
        return super().post(request, *args, **kwargs)
