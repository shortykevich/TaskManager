from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['title']
        labels = {'title': _('Title')}
