from task_manager.users.models import User
from task_manager.users.forms import UsersCreateForm, UsersUpdateForm
from task_manager.core.related_deletion_mixins import DeleteOneToManyMixin
from task_manager.core.users.views_bases import (
    BaseUsersIndexView,
    BaseUsersCreateView,
    BaseUsersUpdateView,
    BaseUsersDeleteView
)


class BaseUserView:
    model = User
    object_name = 'Users'


class UsersIndexView(BaseUserView, BaseUsersIndexView):
    queryset = User.objects.all()


class UsersCreateView(BaseUserView, BaseUsersCreateView):
    form_class = UsersCreateForm
    success_url_name = 'login'


class UsersUpdateView(BaseUserView, BaseUsersUpdateView):
    form_class = UsersUpdateForm
    context_object_name = 'user'
    success_url_name = 'users_index'


class UsersDeleteView(BaseUserView, DeleteOneToManyMixin, BaseUsersDeleteView):
    success_url_name = 'users_index'
