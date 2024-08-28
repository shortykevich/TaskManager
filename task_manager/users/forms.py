from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from task_manager.users.models import User


class UsersBaseForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    usable_password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class UsersCreateForm(UsersBaseForm, BaseUserCreationForm):
    class Meta(UsersBaseForm.Meta):
        pass


class UsersUpdateForm(UsersBaseForm, BaseUserCreationForm):
    class Meta(UsersBaseForm.Meta):
        pass
