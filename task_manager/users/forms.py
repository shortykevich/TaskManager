from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import User


class UsersBaseForm(forms.ModelForm):
    usable_password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
        }

        widgets = {
            'first_name': forms.TextInput,
            'last_name': forms.TextInput,
        }

        required = {'first_name', 'last_name', 'username'}


class UsersCreateForm(UsersBaseForm, BaseUserCreationForm):
    class Meta(UsersBaseForm.Meta):
        pass


class UsersUpdateForm(UsersBaseForm, BaseUserCreationForm):
    class Meta(UsersBaseForm.Meta):
        pass
