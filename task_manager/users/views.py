from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from task_manager.users.forms import UsersCreateForm, UsersUpdateForm
from task_manager.users.models import User


class UserPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs.get('pk'))
        current_user = request.user
        if current_user != user and not current_user.is_superuser:
            messages.error(request, "You are not allowed to edit other users!")
            return redirect('users_index')
        return super().dispatch(request, *args, **kwargs)


class UsersCreateView(CreateView):
    form_class = UsersCreateForm
    template_name = 'users/create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "User created successfully!")
        return super().form_valid(form)


class UsersUpdateView(UserPermissionMixin, UpdateView):
    model = User
    form_class = UsersUpdateForm
    template_name = 'users/update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')

    def form_valid(self, form):
        messages.success(self.request, "User updated successfully!")
        return super().form_valid(form)


class UsersDeleteView(UserPermissionMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users_index')


class UsersIndexView(View):
    def get(self, request):
        return render(
            request,
            'users/index.html',
            context={'users': User.objects.filter(is_staff=False)[:100]}
        )
