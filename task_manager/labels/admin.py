from django.contrib import admin

from task_manager.labels.models import Label


@admin.register(Label)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('name', 'created_at')
