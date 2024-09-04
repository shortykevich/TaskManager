from django.contrib import admin

from task_manager.core.statuses_labels.admin_bases import BaseAdmin
from task_manager.labels.models import Label


@admin.register(Label)
class UsersAdmin(BaseAdmin, admin.ModelAdmin):
    pass
