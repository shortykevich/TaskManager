from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.utils import MsgSuccessMixin, DirectAccessDenialMixin, DeleteManyToManyMixin


class LabelsIndexView(DirectAccessDenialMixin, ListView):
    model = Label
    queryset = Label.objects.all()
    ordering = 'pk'
    context_object_name = 'labels'
    template_name = 'labels/index.html'
    not_authenticated = _('You are not authenticated! Please login.')


class LabelsCreateView(DirectAccessDenialMixin, MsgSuccessMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels_index')
    not_authenticated = _('You are not authenticated! Please login.')
    success_message = _('Your label has been created.')


class LabelsUpdateView(DirectAccessDenialMixin, MsgSuccessMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels_index')
    not_authenticated = _('You are not authenticated! Please login.')
    success_message = _('Your label has been updated.')


class LabelsDeleteView(DirectAccessDenialMixin, DeleteManyToManyMixin):
    model = Label
    context_object_name = 'label'
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Your label has been deleted.')
    not_authenticated = _('You are not authenticated! Please login.')
    error_message = _('Cannot delete a label because it is in use')
