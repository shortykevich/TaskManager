from django.contrib import admin

from task_manager.statuses.models import Status


@admin.register(Status)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('name', 'created_at')
