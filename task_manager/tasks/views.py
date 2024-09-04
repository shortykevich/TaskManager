from task_manager.tasks.forms import TaskForm, TaskFilter
from task_manager.tasks.models import Task
from task_manager.core.tasks.views_bases import (
    BaseTasksDetailView,
    BaseTasksFilterView,
    BaseTasksCreateView,
    BaseTasksUpdateView,
    BaseTasksDeleteView
)


class BaseTasksView:
    model = Task
    object_name = 'Tasks'


class TasksDetailView(BaseTasksView, BaseTasksDetailView):
    pass


class TasksIndexView(BaseTasksView, BaseTasksFilterView):
    filterset_class = TaskFilter

    def get_filterset(self, filterset_class=None):
        filterset_class = self.get_filterset_class()
        return filterset_class(
            self.request.GET,
            queryset=self.get_queryset().order_by('pk'),
            request=self.request,
        )


class TasksCreateView(BaseTasksView, BaseTasksCreateView):
    form_class = TaskForm
    success_url_name = 'tasks_index'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksUpdateView(BaseTasksView, BaseTasksUpdateView):
    model = Task
    form_class = TaskForm
    success_url_name = 'tasks_index'


class TasksDeleteView(BaseTasksView, BaseTasksDeleteView):
    redirect_field_name = None
    success_url_name = 'tasks_index'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.author
