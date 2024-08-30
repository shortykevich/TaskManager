from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from task_manager.users.models import User
from task_manager.users.forms import UsersCreateForm, UsersUpdateForm
from task_manager.utils.ViewsMixins import UserPermissionMixin, SuccessMessageMixin


class UsersCreateView(SuccessMessageMixin, CreateView):
    form_class = UsersCreateForm
    template_name = 'users/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('login')
    success_message = _("User created successfully!")


class UsersUpdateView(UserPermissionMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UsersUpdateForm
    template_name = 'users/update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')
    success_message = _("User updated successfully!")


class UsersDeleteView(UserPermissionMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')
    success_message = _("User deleted successfully!")


class UsersIndexView(ListView):
    template_name = 'users/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_staff=False).order_by('pk')[:100]
