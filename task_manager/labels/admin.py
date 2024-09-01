from django.contrib import admin

from task_manager.labels.models import Label


@admin.register(Label)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'created_at')
    list_filter = ('title', 'created_at')
