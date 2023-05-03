from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django.utils.translation import gettext as _
from django.forms import CheckboxInput, Select

from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import User

from .models import Task


WIDGET = Select(attrs={'class': 'form-control bg-dark text-white'})


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(
        label=_('Status'),
        queryset=Status.objects.all(),
        widget=WIDGET,
    )
    executor = ModelChoiceFilter(
        label=_('Executor'),
        queryset=User.objects.all(),
        widget=WIDGET,
    )
    labels = ModelChoiceFilter(
        label=_('Label'),
        queryset=Label.objects.all(),
        widget=WIDGET,
    )
    only_mine_tasks = BooleanFilter(
        label=_('Only my tasks'),
        method='get_my_tasks',
        widget=CheckboxInput,
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def get_my_tasks(self, queryset, _, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset
