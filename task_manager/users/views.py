from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from task_manager.users.forms import UsersCreateForm, UsersUpdateForm
from task_manager.users.models import User


class UserPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs.get('pk'))
        current_user = request.user
        if not current_user.is_authenticated:
            messages.error(request, _('You are not logged in! Please, log in.'))
            return redirect('login')
        if current_user != user and not current_user.is_superuser:
            messages.error(request, _("You are not allowed to edit other users!"))
            return redirect('users_index')
        return super().dispatch(request, *args, **kwargs)


class UsersCreateView(CreateView):
    form_class = UsersCreateForm
    template_name = 'users/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, _("User created successfully!"))
        return super().form_valid(form)


class UsersUpdateView(UserPermissionMixin, UpdateView):
    model = User
    form_class = UsersUpdateForm
    template_name = 'users/update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')

    def form_valid(self, form):
        messages.success(self.request, _("User updated successfully!"))
        return super().form_valid(form)


class UsersDeleteView(UserPermissionMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')


class UsersIndexView(ListView):
    template_name = 'users/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_staff=False)[:100]
