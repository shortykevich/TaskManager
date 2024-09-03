from task_manager.users.models import User


class UserAuthMixin:
    redirect_field_name = None

    def test_func(self):
        user = User.objects.filter(pk=self.kwargs['pk'])[0]
        return self.request.user == user or self.request.user.is_superuser
