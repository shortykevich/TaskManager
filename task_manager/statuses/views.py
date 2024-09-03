from django.urls import reverse_lazy

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.utils import (
    DeleteOneToManyMixin,
    StatusMessages,
    BaseIndexView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView
)


class StatusesIndexView(StatusMessages, BaseIndexView):
    model = Status
    queryset = Status.objects.all()
    ordering = 'pk'
    context_object_name = 'statuses'
    template_name = 'statuses/index.html'

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        super().__init__(*args, **kwargs)


class StatusesCreateView(StatusMessages, BaseCreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_index')

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_created_msg()
        super().__init__(*args, **kwargs)


class StatusesUpdateView(StatusMessages, BaseUpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses_index')

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_updated_msg()
        super().__init__(*args, **kwargs)


class StatusesDeleteView(StatusMessages, BaseDeleteView, DeleteOneToManyMixin):
    model = Status
    context_object_name = 'status'
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_deleted_msg()
        self.error_message = self.get_error_msg()
        super().__init__(*args, **kwargs)
