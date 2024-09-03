from task_manager.statuses import views
from task_manager.core.urls_dispatcher.dispatcher import generate_crud_urls


urlpatterns = generate_crud_urls(views, 'statuses')
