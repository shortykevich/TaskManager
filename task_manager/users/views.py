from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import UpdateView, CreateView

from task_manager.users.models import User
from task_manager.users.forms import UsersCreateForm, UsersUpdateForm
from task_manager.utils import (
    MsgSuccessMixin,
    DeleteOneToManyMixin,
    UserEditAuthMixin,
    PermissionsMixin
)


class UsersCreateView(MsgSuccessMixin, CreateView):
    form_class = UsersCreateForm
    template_name = 'users/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('login')
    success_message = _('User created successfully!')


class UsersUpdateView(UserEditAuthMixin, PermissionsMixin, MsgSuccessMixin, UpdateView):
    model = User
    form_class = UsersUpdateForm
    template_name = 'users/update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')
    success_message = _('User updated successfully!')
    not_authorized = _('You are not authorized to access this page.')
    not_authenticated = _('You are not authenticated! Please login.')


class UsersDeleteView(UserEditAuthMixin, PermissionsMixin, DeleteOneToManyMixin):
    model = User
    template_name = 'users/delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')
    success_message = _('User deleted successfully!')
    not_authorized = _('You are not authorized to access this page.')
    not_authenticated = _('You are not authenticated! Please login.')
    error_message = _('Cannot delete a user because it is in use')


class UsersIndexView(ListView):
    model = User
    queryset = User.objects.all()
    ordering = 'pk'
    template_name = 'users/index.html'
    context_object_name = 'users'
