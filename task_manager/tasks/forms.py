import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'description', 'status', 'executor', 'labels'
        ]

        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }

        widgets = {
            'title': forms.TextInput,
            'description': forms.Textarea,
            'status': forms.Select,
            'executor': forms.Select,
            'labels': forms.SelectMultiple,
        }


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        field_name='status',
        queryset=Status.objects.all(),
        label=_('Status'),
    )
    executor = django_filters.ModelChoiceFilter(
        field_name='executor',
        queryset=User.objects.all(),
        label=_('Executor'),
    )
    labels = django_filters.ModelChoiceFilter(
        field_name='labels',
        queryset=Label.objects.all(),
        label=_('Label'),
    )

    class Meta:
        model = Task

        fields = {
            'status': ['exact'],
            'executor': ['exact'],
            'labels': ['exact'],
        }

    self_tasks = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        method='filter_self_tasks',
        label=_('Only my tasks'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.data:
            self.is_bound = False

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
