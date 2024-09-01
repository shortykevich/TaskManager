from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from task_manager.utils import DirectAccessDenialMixin, MsgSuccessMixin, PermissionsMixin
from task_manager.tasks.forms import TaskForm, TaskFilter
from task_manager.tasks.models import Task


class TasksDetailView(DirectAccessDenialMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_page.html'
    not_authenticated = _('You are not authenticated! Please login.')


class TasksIndexView(DirectAccessDenialMixin, MsgSuccessMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'
    not_authenticated = _('You are not authenticated! Please login.')

    def get_filterset(self, filterset_class=None):
        filterset_class = self.get_filterset_class()
        return filterset_class(
            self.request.GET,
            queryset=self.get_queryset().order_by('pk'),
            request=self.request,
        )


class TasksCreateView(DirectAccessDenialMixin, MsgSuccessMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task created successfully')
    not_authenticated = _('You are not authenticated! Please login.')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksUpdateView(DirectAccessDenialMixin, MsgSuccessMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task updated successfully')
    not_authenticated = _('You are not authenticated! Please login.')


class TasksDeleteView(PermissionsMixin, MsgSuccessMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    redirect_field_name = None
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task deleted successfully')
    not_authorized = _('Only author can delete task')
    not_authenticated = _('You are not authenticated! Please login.')

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.author
