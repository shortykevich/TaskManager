from task_manager.core.statuses_labels.views_bases import ViewsFactory


StatusViews = ViewsFactory('Status')

StatusesIndexView = StatusViews.get_index_view()
StatusesCreateView = StatusViews.get_create_view()
StatusesUpdateView = StatusViews.get_update_view()
StatusesDeleteView = StatusViews.get_delete_view()
