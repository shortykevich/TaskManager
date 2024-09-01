from django.contrib import admin

from task_manager.statuses.models import Status


@admin.register(Status)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'created_at')
    list_filter = ('title', 'created_at')
