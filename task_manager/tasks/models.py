from django.db import models

from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        null=False,
    )
    description = models.TextField(null=False,)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='task_author',
        null=False,
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='task_executor',
        null=False,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='task_status',
        null=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
