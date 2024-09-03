from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class DirectAccessDenialMixin(LoginRequiredMixin):
    redirect_field_name = None

    def handle_no_permission(self):
        messages.error(self.request, self.not_authenticated)
        return super().handle_no_permission()
