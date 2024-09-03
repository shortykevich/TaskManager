from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.utils import (
    DeleteOneToManyMixin,
    BaseIndexView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView
)


class BaseStatusView:
    model = Status
    object_name = 'Statuses'
    success_url_name = 'statuses_index'


class StatusesIndexView(BaseStatusView, BaseIndexView):
    queryset = Status.objects.all()


class StatusesCreateView(BaseStatusView, BaseCreateView):
    form_class = StatusForm


class StatusesUpdateView(BaseStatusView, BaseUpdateView):
    form_class = StatusForm


class StatusesDeleteView(BaseStatusView, BaseDeleteView, DeleteOneToManyMixin):
    pass
