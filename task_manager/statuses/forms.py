from django import forms
from django.forms import ModelForm
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _


class StatusForm(ModelForm):
    title = forms.CharField(
        label=_('Title'),
    )
    class Meta:
        model = Status
        fields = ['title']
