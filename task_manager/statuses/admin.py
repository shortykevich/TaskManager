from django.contrib import admin

from task_manager.core.statuses_labels.admin_bases import BaseAdmin
from task_manager.statuses.models import Status


@admin.register(Status)
class UsersAdmin(BaseAdmin, admin.ModelAdmin):
    pass
