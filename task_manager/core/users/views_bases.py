from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from task_manager.core.permissions_mixin import PermissionsMixin
from task_manager.core.users.mixins import UserAuthMixin
from task_manager.core.messages_mixins import MsgSuccessMixin
from task_manager.core.base_views import BaseObjectView


class BaseUsersIndexView(BaseObjectView, ListView):
    ordering = 'pk'
    context_object_name = None

    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/index.html'
        self.context_object_name = f'{self.object_name.lower()}'


class BaseUsersCreateView(BaseObjectView, MsgSuccessMixin, CreateView):
    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/create.html'
        self.success_message = super().get_created()


class BaseUsersUpdateView(
    UserAuthMixin, PermissionsMixin, BaseObjectView, MsgSuccessMixin, UpdateView
):
    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/update.html'
        self.not_authorized = super().get_not_authorized()
        self.not_authenticated = super().get_not_authenticated()
        self.success_message = super().get_updated()


class BaseUsersDeleteView(UserAuthMixin, PermissionsMixin, BaseObjectView, DeleteView):
    context_object_name = None

    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/delete.html'
        self.context_object_name = f'{self.object_name.lower()}'
        self.not_authenticated = super().get_not_authenticated()
        self.not_authorized = super().get_not_authorized()
        self.success_message = super().get_deleted()
        self.error_message = super().get_error()
