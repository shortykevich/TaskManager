from django.utils.translation import gettext_lazy as _
from django.contrib import messages


class MsgSuccessMixin:
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class BaseMessages:

    @classmethod
    def _get_message(cls, action):
        msgs = {
            'UserMsgs': {
                'created': _('User created successfully'),
                'updated': _('User updated successfully'),
                'deleted': _('User deleted successfully'),
                'error': _('Cannot delete a user because it is in use'),
            },
            'TaskMsgs': {
                'created': _('Task created successfully'),
                'updated': _('Task updated successfully'),
                'deleted': _('Task deleted successfully'),
            },
            'StatusMsgs': {
                'created': _('Status created successfully'),
                'updated': _('Status updated successfully'),
                'deleted': _('Status deleted successfully'),
                'error': _('Cannot delete a status because it is in use'),
            },
            'LabelMsgs': {
                'created': _('Label created successfully'),
                'updated': _('Label updated successfully'),
                'deleted': _('Label deleted successfully'),
                'error': _('Cannot delete a label because it is in use'),
            }
        }
        return msgs.get(cls.__name__).get(action)

    @staticmethod
    def not_authenticated():
        return _('You are not authenticated! Please login.')

    @staticmethod
    def not_authorized():
        return _('You are not authorized to access this page.')

    @classmethod
    def created(cls):
        return cls._get_message('created')

    @classmethod
    def updated(cls):
        return cls._get_message('updated')

    @classmethod
    def deleted(cls):
        return cls._get_message('deleted')

    @classmethod
    def error(cls):
        return cls._get_message('error')


class TaskMsgs(BaseMessages):
    @staticmethod
    def not_authorized():
        return _('Only the author can delete a task')


class UserMsgs(BaseMessages):
    pass


class StatusMsgs(BaseMessages):
    pass


class LabelMsgs(BaseMessages):
    pass
