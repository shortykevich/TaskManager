from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from task_manager.core.related_deletion_mixins import (
    DeleteOneToManyMixin,
    DeleteManyToManyMixin
)
from task_manager.core.base_views import (
    BaseIndexView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView
)


class ViewsFactory:
    _models = {
        'Status': Status,
        'Label': Label,
    }
    _forms = {
        'Status': StatusForm,
        'Label': LabelForm,
    }
    _plural_endings = {
        'Status': 'es',
        'Label': 's',
    }
    _deletion_handlers = {
        'Status': DeleteOneToManyMixin,
        'Label': DeleteManyToManyMixin,
    }

    def __init__(self, app_name):
        self.app_name = app_name

    @property
    def ending(self):
        return self._plural_endings[self.app_name]

    @property
    def model(self):
        return self._models[self.app_name]

    @property
    def form(self):
        return self._forms[self.app_name]

    @property
    def deletion_handler(self):
        return self._deletion_handlers[self.app_name]

    def get_base_view(self):
        class BaseView:
            model = self.model
            object_name = f'{self.app_name}{self.ending}'
            success_url_name = f'{self.app_name}{self.ending}_index'.lower()
        return BaseView

    def get_index_view(self):
        base = self.get_base_view()

        class IndexView(base, BaseStLbIndexView):
            pass
        return IndexView

    def get_create_view(self):
        base = self.get_base_view()

        class CreateView(base, BaseStLbCreateView):
            form_class = self.form
        return CreateView

    def get_update_view(self):
        base = self.get_base_view()

        class UpdateView(base, BaseStLbUpdateView):
            form_class = self.form
        return UpdateView

    def get_delete_view(self):
        base = self.get_base_view()
        handler = self.deletion_handler

        class DeleteView(base, handler, BaseStLbDeleteView):
            pass
        return DeleteView


class BaseStLbIndexView(BaseIndexView):
    context_object_name = None

    def __init__(self):
        super().__init__()
        self.context_object_name = f'{self.object_name.lower()}'
        self.not_authenticated = super().get_not_authenticated()

    def get_queryset(self):
        return self.model.objects.all()


class BaseStLbCreateView(BaseCreateView):

    def __init__(self):
        super().__init__()
        self.not_authenticated = super().get_not_authenticated()
        self.success_message = super().get_created()


class BaseStLbUpdateView(BaseUpdateView):

    def __init__(self):
        super().__init__()
        self.not_authenticated = super().get_not_authenticated()
        self.success_message = super().get_updated()


class BaseStLbDeleteView(BaseDeleteView):
    context_object_name = None

    def __init__(self):
        super().__init__()
        self.context_object_name = f'{self.object_name.lower()}'
        self.not_authenticated = super().get_not_authenticated()
        self.success_message = super().get_deleted()
        self.error_message = super().get_error()
