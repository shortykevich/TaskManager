from django.contrib import admin

from task_manager.tasks.models import Task


@admin.register(Task)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'status', 'executor')
    search_fields = ('name', 'created_at')
    list_filter = ('status', 'executor')
