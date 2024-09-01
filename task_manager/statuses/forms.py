from django.forms import ModelForm
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['title']
        labels = {'title': _('Title')}
