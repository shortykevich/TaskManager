from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.utils import (
    DeleteManyToManyMixin,
    BaseIndexView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView
)


class BaseLabelView:
    model = Label
    object_name = 'Labels'
    success_url_name = 'labels_index'


class LabelsIndexView(BaseLabelView, BaseIndexView):
    queryset = Label.objects.all()


class LabelsCreateView(BaseLabelView, BaseCreateView):
    form_class = LabelForm


class LabelsUpdateView(BaseLabelView, BaseUpdateView):
    form_class = LabelForm


class LabelsDeleteView(BaseLabelView, BaseDeleteView, DeleteManyToManyMixin):
    pass
