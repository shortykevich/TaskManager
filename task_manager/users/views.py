from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from task_manager.users.forms import UsersCreateForm, UsersUpdateForm
from task_manager.users.models import User


class UserPermissionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        current_user = request.user
        not_authenticated = _('You are not authenticated! Please login.')
        not_authorized = _('You are not authorized to access this page.')
        if current_user.is_anonymous:
            messages.error(request, not_authenticated)
            return redirect(self.login_url)
        elif user != current_user and not current_user.is_superuser:
            messages.error(request, not_authorized)
            return redirect('users_index')
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class UsersCreateView(CreateView):
    form_class = UsersCreateForm
    template_name = 'users/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('login')
    success_message = _("User created successfully!")


class UsersUpdateView(UserPermissionMixin, UpdateView):
    model = User
    form_class = UsersUpdateForm
    template_name = 'users/update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')
    success_message = _("User updated successfully!")


class UsersDeleteView(UserPermissionMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')
    success_message = _("User deleted successfully!")


class UsersIndexView(ListView):
    template_name = 'users/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_staff=False)[:100]
