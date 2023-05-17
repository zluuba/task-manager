from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.urls import reverse_lazy

from task_manager.utils import AuthorizationCheckMixin
from task_manager.tasks.models import Task

from .models import Label
from .forms import LabelForm


class LabelsView(AuthorizationCheckMixin, ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'labels/labels.html'


class LabelCreateView(AuthorizationCheckMixin,
                      SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created')


class LabelUpdateView(AuthorizationCheckMixin,
                      SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully updated')


class LabelDeleteView(AuthorizationCheckMixin,
                      SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')

    def post(self, request, *args, **kwargs):
        label_id = kwargs['pk']
        tasks_with_label = Task.objects.filter(labels=label_id)

        if tasks_with_label:
            messages.error(
                self.request,
                _('It is not possible to delete a label '
                  'because it is in use')
            )
            return redirect('labels')
        return super().post(request, *args, **kwargs)
