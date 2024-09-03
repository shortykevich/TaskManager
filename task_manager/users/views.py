from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView

from task_manager.users.models import User
from task_manager.users.forms import UsersCreateForm, UsersUpdateForm
from task_manager.utils import (
    MsgSuccessMixin,
    DeleteOneToManyMixin,
    UserEditAuthMixin,
    PermissionsMixin,
    UserMsgs
)


class UsersCreateView(UserMsgs, MsgSuccessMixin, CreateView):
    form_class = UsersCreateForm
    template_name = 'users/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('login')

    def __init__(self, *args, **kwargs):
        self.success_message = UserMsgs.created()
        super().__init__(*args, **kwargs)


class UsersUpdateView(UserMsgs, UserEditAuthMixin, PermissionsMixin, MsgSuccessMixin, UpdateView):
    model = User
    form_class = UsersUpdateForm
    template_name = 'users/update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')
    success_message = UserMsgs.updated()
    not_authorized = UserMsgs.not_authorized()
    not_authenticated = UserMsgs.not_authenticated()


class UsersDeleteView(UserMsgs, UserEditAuthMixin, PermissionsMixin, DeleteOneToManyMixin):
    model = User
    template_name = 'users/delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')
    success_message = UserMsgs.deleted()
    not_authorized = UserMsgs.not_authorized()
    not_authenticated = UserMsgs.not_authenticated()
    error_message = UserMsgs.error()


class UsersIndexView(ListView):
    model = User
    queryset = User.objects.all()
    ordering = 'pk'
    template_name = 'users/index.html'
    context_object_name = 'users'
