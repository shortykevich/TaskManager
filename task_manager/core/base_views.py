from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from task_manager.core.direct_access_mixin import DirectAccessDenialMixin
from task_manager.core.messages_mixins import (
    StatusMsgs,
    LabelMsgs,
    UserMsgs,
    TaskMsgs,
    MsgSuccessMixin
)


class BaseObjectView:
    msg_classes = {
        'statuses': StatusMsgs,
        'labels': LabelMsgs,
        'users': UserMsgs,
        'tasks': TaskMsgs,
    }
    template_name = None
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

    def get_not_authorized(self):
        return self.messages.not_authorized()

    def get_created(self):
        return self.messages.created()

    def get_updated(self):
        return self.messages.updated()

    def get_deleted(self):
        return self.messages.deleted()

    def get_error(self):
        return self.messages.error()


class BaseDetailView(DirectAccessDenialMixin, BaseObjectView, DetailView):
    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/detail.html'


class BaseFilterView(DirectAccessDenialMixin, BaseObjectView, FilterView):
    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/index.html'

    def get_filterset(self, filterset_class=None):
        filterset_class = self.get_filterset_class()
        return filterset_class(
            self.request.GET,
            queryset=self.get_queryset().order_by('pk'),
            request=self.request,
        )


class BaseIndexView(DirectAccessDenialMixin, BaseObjectView, ListView):
    ordering = 'pk'

    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/index.html'


class BaseCreateView(DirectAccessDenialMixin, BaseObjectView, MsgSuccessMixin, CreateView):
    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/create.html'


class BaseUpdateView(DirectAccessDenialMixin, BaseObjectView, MsgSuccessMixin, UpdateView):
    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/update.html'


class BaseDeleteView(DirectAccessDenialMixin, BaseObjectView, MsgSuccessMixin, DeleteView):
    def __init__(self):
        super().__init__()
        self.template_name = f'{self.object_name.lower()}/delete.html'
