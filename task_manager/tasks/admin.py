from django.contrib import admin
from task_manager.tasks.models import Task


@admin.register(Task)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'executor')
    search_fields = ('title', 'created_at')
    list_filter = ('status', 'executor')
