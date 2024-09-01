from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin


class DirectAccessDenialMixin(LoginRequiredMixin):
    redirect_field_name = None

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authenticated! Please login.'))
        return super().handle_no_permission()