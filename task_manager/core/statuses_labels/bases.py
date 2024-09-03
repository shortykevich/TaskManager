from task_manager.core.base_views import (
    BaseIndexView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView
)


class BaseStLbIndexView(BaseIndexView):
    context_object_name = None

    def __init__(self):
        super().__init__()
        self.context_object_name = f'{self.object_name.lower()}'
        self.not_authenticated = super().get_not_authenticated()


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
