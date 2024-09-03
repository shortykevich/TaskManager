from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from task_manager.utils.direct_access_mixin import DirectAccessDenialMixin
from task_manager.utils.messages_mixins import MsgSuccessMixin
from task_manager.utils.messages_mixins import StatusMsgs, LabelMsgs


class BaseObjectView:
    msg_classes = {
        'statuses': StatusMsgs,
        'labels': LabelMsgs,
    }
    success_url_name = None
    object_name = None

    @property
    def success_url(self):
        return reverse_lazy(self.success_url_name)

    @property
    def messages(self):
        return self.msg_classes.get(self.object_name.lower())

    def get_not_authenticated(self):
        return self.messages.not_authenticated()

    def get_created(self):
        return self.messages.created()

    def get_updated(self):
        return self.messages.updated()

    def get_deleted(self):
        return self.messages.deleted()

    def get_error(self):
        return self.messages.error()


class BaseIndexView(BaseObjectView, DirectAccessDenialMixin, ListView):
    ordering = 'pk'
    context_object_name = None

    def __init__(self):
        super().__init__()
        self.context_object_name = f'{self.object_name.lower()}'
        self.template_name = f'{self.object_name.lower()}/index.html'
        self.not_authenticated = super().get_not_authenticated()


class BaseCreateView(BaseObjectView, DirectAccessDenialMixin, MsgSuccessMixin, CreateView):
    template_name = None

    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/create.html'
        self.not_authenticated = super().get_not_authenticated()
        self.success_message = super().get_created()


class BaseUpdateView(BaseObjectView, DirectAccessDenialMixin, MsgSuccessMixin, UpdateView):
    template_name = None

    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/update.html'
        self.not_authenticated = super().get_not_authenticated()
        self.success_message = super().get_updated()


class BaseDeleteView(BaseObjectView, DirectAccessDenialMixin):
    context_object_name = None
    template_name = None

    def __init__(self):
        super().__init__()
        self.context_object_name = self.object_name.lower()
        self.template_name = f'{self.object_name.lower()}/delete.html'
        self.not_authenticated = super().get_not_authenticated()
        self.success_message = super().get_deleted()
        self.error_message = super().get_error()
