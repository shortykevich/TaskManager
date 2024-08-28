from django.contrib.auth.forms import AuthenticationForm
from task_manager.users.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
