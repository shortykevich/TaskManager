from django.contrib import admin

from task_manager.users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = (('date_joined', admin.DateFieldListFilter),)
