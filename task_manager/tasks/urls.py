from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.TasksIndexView.as_view(), name='index'),
]