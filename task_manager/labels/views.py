from django.urls import reverse_lazy

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.utils import (
    DeleteManyToManyMixin,
    LabelMessages,
    BaseIndexView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView
)


class LabelsIndexView(LabelMessages, BaseIndexView):
    model = Label
    queryset = Label.objects.all()
    ordering = 'pk'
    context_object_name = 'labels'
    template_name = 'labels/index.html'

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        super().__init__(*args, **kwargs)


class LabelsCreateView(LabelMessages, BaseCreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels_index')

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_created_msg()
        super().__init__(*args, **kwargs)


class LabelsUpdateView(LabelMessages, BaseUpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels_index')

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_updated_msg()
        super().__init__(*args, **kwargs)


class LabelsDeleteView(LabelMessages, BaseDeleteView, DeleteManyToManyMixin):
    model = Label
    context_object_name = 'label'
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_deleted_msg()
        self.error_message = self.get_error_msg()
        super().__init__(*args, **kwargs)
