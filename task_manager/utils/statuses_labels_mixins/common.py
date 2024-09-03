from django.views.generic import ListView, CreateView, UpdateView

from task_manager.utils.direct_access_mixin import DirectAccessDenialMixin
from task_manager.utils.messages_mixins import MsgSuccessMixin


class BaseIndexView(DirectAccessDenialMixin, ListView):
    ordering = 'pk'
    pass


class BaseCreateView(DirectAccessDenialMixin, MsgSuccessMixin, CreateView):
    pass


class BaseUpdateView(DirectAccessDenialMixin, MsgSuccessMixin, UpdateView):
    pass


class BaseDeleteView(DirectAccessDenialMixin):
    pass
