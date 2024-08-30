from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.utils.ViewsMixins import StatusesPermissionMixin, SuccessMessageMixin


class StatusesIndexView(StatusesPermissionMixin, SuccessMessageMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/index.html'

    def get_queryset(self):
        return Status.objects.all().order_by('pk')[:100]


class StatusesCreateView(StatusesPermissionMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Your status has been created.')


class StatusesUpdateView(StatusesPermissionMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Your status has been updated.')


class StatusesDeleteView(StatusesPermissionMixin, SuccessMessageMixin, DeleteView):
    model = Status
    context_object_name = 'status'
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Your status has been deleted.')
