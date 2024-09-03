from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.core.related_deletion_mixins import DeleteOneToManyMixin
from task_manager.core.statuses_labels.bases import (
    BaseStLbIndexView,
    BaseStLbCreateView,
    BaseStLbUpdateView,
    BaseStLbDeleteView
)


class BaseStatusView:
    model = Status
    object_name = 'Statuses'
    success_url_name = 'statuses_index'


class StatusesIndexView(BaseStatusView, BaseStLbIndexView):
    queryset = Status.objects.all()


class StatusesCreateView(BaseStatusView, BaseStLbCreateView):
    form_class = StatusForm


class StatusesUpdateView(BaseStatusView, BaseStLbUpdateView):
    form_class = StatusForm


class StatusesDeleteView(BaseStatusView, BaseStLbDeleteView, DeleteOneToManyMixin):
    pass
