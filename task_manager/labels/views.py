from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.core.related_deletion_mixins import DeleteManyToManyMixin
from task_manager.core.statuses_labels.bases import (
    BaseStLbIndexView,
    BaseStLbCreateView,
    BaseStLbUpdateView,
    BaseStLbDeleteView
)


class BaseLabelView:
    model = Label
    object_name = 'Labels'
    success_url_name = 'labels_index'


class LabelsIndexView(BaseLabelView, BaseStLbIndexView):
    queryset = Label.objects.all()


class LabelsCreateView(BaseLabelView, BaseStLbCreateView):
    form_class = LabelForm


class LabelsUpdateView(BaseLabelView, BaseStLbUpdateView):
    form_class = LabelForm


class LabelsDeleteView(BaseLabelView, BaseStLbDeleteView, DeleteManyToManyMixin):
    pass
