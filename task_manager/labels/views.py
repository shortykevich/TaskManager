from task_manager.core.statuses_labels.views_bases import ViewsFactory


LabelsViews = ViewsFactory('Label')

LabelsIndexView = LabelsViews.get_index_view()
LabelsCreateView = LabelsViews.get_create_view()
LabelsUpdateView = LabelsViews.get_update_view()
LabelsDeleteView = LabelsViews.get_delete_view()
