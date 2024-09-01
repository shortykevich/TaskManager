from django.forms import ModelForm

from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['title']
        labels = {'title': _('Title')}
