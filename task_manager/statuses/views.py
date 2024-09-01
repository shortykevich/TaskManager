from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.utils import MsgSuccessMixin, DirectAccessDenialMixin, DeleteRelatedMixin


class StatusesIndexView(DirectAccessDenialMixin, MsgSuccessMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/index.html'

    def get_queryset(self):
        return Status.objects.all().order_by('pk')


class StatusesCreateView(DirectAccessDenialMixin, MsgSuccessMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Your status has been created.')


class StatusesUpdateView(DirectAccessDenialMixin, MsgSuccessMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Your status has been updated.')


class StatusesDeleteView(DirectAccessDenialMixin, DeleteRelatedMixin):
    model = Status
    context_object_name = 'status'
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Your status has been deleted.')
    error_message = _('Cannot delete a status because it is in use')
