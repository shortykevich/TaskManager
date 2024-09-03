from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class PermissionsMixin(LoginRequiredMixin, UserPassesTestMixin):
    redirect_field_name = None

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.not_authenticated)
            return super().handle_no_permission()
        messages.error(self.request, self.not_authorized)
        return redirect(self.success_url)
