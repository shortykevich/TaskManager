from django.utils.translation import gettext_lazy as _
from django.contrib import messages


class MsgSuccessMixin:
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class BaseMessages:
    _not_authenticated = _('You are not authenticated! Please login.')
    _not_authorized = _('You are not authorized to access this page.')

    def get_not_authenticated_msg(self):
        return self._not_authenticated

    def get_not_authorized_msg(self):
        return self._not_authorized

    def get_error_msg(self):
        return self._error_message

    def get_created_msg(self):
        return self._created

    def get_updated_msg(self):
        return self._updated

    def get_deleted_msg(self):
        return self._deleted


class UserMsgs(BaseMessages):
    _created = _('User created successfully')
    _updated = _('User updated successfully')
    _deleted = _('User deleted successfully')
    _error_message = _('Cannot delete a user because it is in use')


class TaskMessages(BaseMessages):
    _not_authorized = _('Only author can delete task')
    _created = _('Task created successfully')
    _updated = _('Task updated successfully')
    _deleted = _('Task deleted successfully')


class StatusMessages(BaseMessages):
    _created = _('Status created successfully')
    _updated = _('Status updated successfully')
    _deleted = _('Status deleted successfully')
    _error_message = _('Cannot delete a status because it is in use')


class LabelMessages(BaseMessages):
    _created = _('Label created successfully')
    _updated = _('Label updated successfully')
    _deleted = _('Label deleted successfully')
    _error_message = _('Cannot delete a label because it is in use')
