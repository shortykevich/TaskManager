from django.shortcuts import get_object_or_404

from task_manager.users.models import User


class UserEditAuthMixin:
    redirect_field_name = None

    def test_func(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return self.request.user == user or self.request.user.is_superuser
