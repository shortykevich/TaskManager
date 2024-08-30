from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class StatusesPermissionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('home')

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authenticated! Please login.'))
        return redirect(self.login_url)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class StatusesIndexView(StatusesPermissionMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/index.html'

    def get_queryset(self):
        return Status.objects.all()[:100]


class StatusesCreateView(StatusesPermissionMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Your status has been created.')


class StatusesUpdateView(StatusesPermissionMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Your status has been updated.')


class StatusesDeleteView(StatusesPermissionMixin, DeleteView):
    model = Status
    context_object_name = 'status'
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Your status has been deleted.')
