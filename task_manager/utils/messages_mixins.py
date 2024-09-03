from django.utils.translation import gettext_lazy as _
from django.contrib import messages


class MsgSuccessMixin:
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class BaseMessages:
    @staticmethod
    def not_authenticated():
        return _('You are not authenticated! Please login.')

    @staticmethod
    def not_authorized():
        return _('You are not authorized to access this page.')

    @staticmethod
    def created():
        pass

    @staticmethod
    def updated():
        pass

    @staticmethod
    def deleted():
        pass

    @staticmethod
    def error():
        pass


class UserMsgs(BaseMessages):
    @staticmethod
    def created():
        return _('User created successfully')

    @staticmethod
    def updated():
        return _('User updated successfully')

    @staticmethod
    def deleted():
        return _('User deleted successfully')

    @staticmethod
    def error():
        return _('Cannot delete a user because it is in use')


class TaskMsgs(BaseMessages):
    @staticmethod
    def not_authorized():
        return _('Only author can delete task')

    @staticmethod
    def created():
        return _('Task created successfully')

    @staticmethod
    def updated():
        return _('Task updated successfully')

    @staticmethod
    def deleted():
        return _('Task deleted successfully')


class StatusMsgs(BaseMessages):
    @staticmethod
    def created():
        return _('Status created successfully')

    @staticmethod
    def updated():
        return _('Status updated successfully')

    @staticmethod
    def deleted():
        return _('Status deleted successfully')

    @staticmethod
    def error():
        return _('Cannot delete a status because it is in use')


class LabelMsgs(BaseMessages):
    @staticmethod
    def created():
        return _('Label created successfully')

    @staticmethod
    def updated():
        return _('Label updated successfully')

    @staticmethod
    def deleted():
        return _('Label deleted successfully')

    @staticmethod
    def error():
        return _('Cannot delete a label because it is in use')
