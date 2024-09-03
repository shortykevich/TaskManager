from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from task_manager.tasks.forms import TaskForm, TaskFilter
from task_manager.tasks.models import Task
from task_manager.utils import (
    DirectAccessDenialMixin,
    MsgSuccessMixin,
    PermissionsMixin,
    TaskMessages
)


class TasksDetailView(TaskMessages, DirectAccessDenialMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_page.html'

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        super().__init__(*args, **kwargs)


class TasksIndexView(TaskMessages, DirectAccessDenialMixin, MsgSuccessMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        super().__init__(*args, **kwargs)

    def get_filterset(self, filterset_class=None):
        filterset_class = self.get_filterset_class()
        return filterset_class(
            self.request.GET,
            queryset=self.get_queryset().order_by('pk'),
            request=self.request,
        )


class TasksCreateView(TaskMessages, DirectAccessDenialMixin, MsgSuccessMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks_index')

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_created_msg()
        super().__init__(*args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksUpdateView(TaskMessages, DirectAccessDenialMixin, MsgSuccessMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks_index')

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.success_message = self.get_updated_msg()
        super().__init__(*args, **kwargs)


class TasksDeleteView(TaskMessages, PermissionsMixin, MsgSuccessMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    redirect_field_name = None
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_index')

    def __init__(self, *args, **kwargs):
        self.not_authenticated = self.get_not_authenticated_msg()
        self.not_authorized = self.get_not_authorized_msg()
        self.success_message = self.get_deleted_msg()
        super().__init__(*args, **kwargs)

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.author
