from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
)
from django.utils.translation import gettext_lazy as _
from task_manager.forms import LoginForm


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class LoginView(BaseLoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_field_name = None
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, _('You are now logged in!'))
        return super().form_valid(form)


class LogoutView(BaseLogoutView):
    def post(self, request, *args, **kwargs):
        messages.info(request, _('You are now logged out.'))
        return super().post(request, *args, **kwargs)
