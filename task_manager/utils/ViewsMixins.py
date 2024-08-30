from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.users.models import User



class StatusesPermissionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('home')

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authenticated! Please login.'))
        return redirect(self.login_url)


class UserPermissionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('home')
    not_authenticated = _('You are not authenticated! Please login.')
    not_authorized = _('You are not authorized to access this page.')

    def dispatch(self, request, *args, **kwargs):
        current_user = request.user
        if current_user.is_anonymous:
            messages.error(request, self.not_authenticated)
            return redirect(self.login_url)

        user = User.objects.get(pk=kwargs['pk'])
        if user != current_user and not current_user.is_superuser:
            messages.error(request, self.not_authorized)
            return redirect('users_index')
        return super().dispatch(request, *args, **kwargs)


class SuccessMessageMixin:
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

