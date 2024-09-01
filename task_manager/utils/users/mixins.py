from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from task_manager.users.models import User


class UserEditAuthMixin(LoginRequiredMixin, UserPassesTestMixin):
    redirect_field_name = None
    not_authorized = _('You are not authorized to access this page.')

    def test_func(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return self.request.user == user or self.request.user.is_superuser

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.not_authenticated)
            return super().handle_no_permission()
        messages.error(self.request, self.not_authorized)
        return redirect(self.success_url)
