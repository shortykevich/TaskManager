from django.urls import path

from task_manager.tasks import views
from task_manager.core.urls_dispatcher.dispatcher import generate_crud_urls


urlpatterns = generate_crud_urls(views, 'tasks')

urlpatterns += [
    path('<int:pk>', views.TasksDetailView.as_view(), name='tasks_detail'),
]
