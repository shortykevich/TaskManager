from django.views.generic import ListView, CreateView, UpdateView

from task_manager.utils.direct_access_mixin import DirectAccessDenialMixin
from task_manager.utils.messages_mixins import MsgSuccessMixin


class BaseIndexView(DirectAccessDenialMixin, ListView):
    ordering = 'pk'

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        super().__init__(*args, **kwargs)


class BaseCreateView(DirectAccessDenialMixin, MsgSuccessMixin, CreateView):
    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_created_msg()
        super().__init__(*args, **kwargs)


class BaseUpdateView(DirectAccessDenialMixin, MsgSuccessMixin, UpdateView):
    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_updated_msg()
        super().__init__(*args, **kwargs)


class BaseDeleteView(DirectAccessDenialMixin):
    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_deleted_msg()
        self.error_message = self.get_error_msg()
        super().__init__(*args, **kwargs)
