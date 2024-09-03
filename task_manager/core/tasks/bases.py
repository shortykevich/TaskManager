from task_manager.core.permissions_mixin import PermissionsMixin
from task_manager.core.base_views import (
    BaseDetailView,
    BaseFilterView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView
)


class BaseTasksDetailView(BaseDetailView):
    def __init__(self):
        super().__init__()
        self.context_object_name = f'{self.object_name.lower()}'
        self.not_authenticated = super().get_not_authenticated()


class BaseTasksFilterView(BaseFilterView):
    context_object_name = None

    def __init__(self):
        super().__init__()
        self.context_object_name = f'{self.object_name.lower()}'
        self.not_authenticated = super().get_not_authenticated()


class BaseTasksCreateView(BaseCreateView):

    def __init__(self):
        super().__init__()
        self.success_message = super().get_created()
        self.not_authenticated = super().get_not_authenticated()
        self.success_message = super().get_created()


class BaseTasksUpdateView(BaseUpdateView):

    def __init__(self):
        super().__init__()
        self.not_authenticated = super().get_not_authenticated()
        self.success_message = super().get_updated()


class BaseTasksDeleteView(BaseDeleteView, PermissionsMixin):
    context_object_name = None

    def __init__(self):
        super().__init__()
        self.context_object_name = f'{self.object_name.lower()}'
        self.not_authenticated = super().get_not_authenticated()
        self.not_authorized = super().get_not_authorized()
        self.success_message = super().get_deleted()
