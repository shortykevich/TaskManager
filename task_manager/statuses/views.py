from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.utils import MsgSuccessMixin, DirectAccessDenialMixin, DeleteOneToManyMixin


class StatusesIndexView(DirectAccessDenialMixin, ListView):
    model = Status
    queryset = Status.objects.all()
    ordering = 'pk'
    context_object_name = 'statuses'
    template_name = 'statuses/index.html'
    not_authenticated = _('You are not authenticated! Please login.')


class StatusesCreateView(DirectAccessDenialMixin, MsgSuccessMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_index')
    not_authenticated = _('You are not authenticated! Please login.')
    success_message = _('Your status has been created.')


class StatusesUpdateView(DirectAccessDenialMixin, MsgSuccessMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses_index')
    not_authenticated = _('You are not authenticated! Please login.')
    success_message = _('Your status has been updated.')


class StatusesDeleteView(DirectAccessDenialMixin, DeleteOneToManyMixin):
    model = Status
    context_object_name = 'status'
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Your status has been deleted.')
    not_authenticated = _('You are not authenticated! Please login.')
    error_message = _('Cannot delete a status because it is in use')
