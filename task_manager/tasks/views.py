from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from task_manager.tasks.forms import TaskForm, TaskFilter
from task_manager.tasks.models import Task
from task_manager.utils import (
    DirectAccessDenialMixin,
    MsgSuccessMixin,
    PermissionsMixin,
    TaskMsgs
)


class TasksDetailView(TaskMsgs, DirectAccessDenialMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_page.html'
    not_authenticated = TaskMsgs.not_authenticated()


class TasksIndexView(TaskMsgs, DirectAccessDenialMixin, MsgSuccessMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'
    not_authenticated = TaskMsgs.not_authenticated()

    def get_filterset(self, filterset_class=None):
        filterset_class = self.get_filterset_class()
        return filterset_class(
            self.request.GET,
            queryset=self.get_queryset().order_by('pk'),
            request=self.request,
        )


class TasksCreateView(TaskMsgs, DirectAccessDenialMixin, MsgSuccessMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks_index')
    not_authenticated = TaskMsgs.not_authenticated()
    success_message = TaskMsgs.created()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksUpdateView(TaskMsgs, DirectAccessDenialMixin, MsgSuccessMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks_index')
    not_authenticated = TaskMsgs.not_authenticated()
    success_message = TaskMsgs.updated()


class TasksDeleteView(TaskMsgs, PermissionsMixin, MsgSuccessMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    redirect_field_name = None
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_index')
    not_authenticated = TaskMsgs.not_authenticated()
    not_authorized = TaskMsgs.not_authorized()
    success_message = TaskMsgs.deleted()

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.author
