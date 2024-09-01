from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import User


class Task(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        verbose_name=_('Title'),
    )
    description = models.TextField(null=False,)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='task_author',
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='task_executor',
        null=True,
        blank=True,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='task_status',
        null=False,
    )
    labels = models.ManyToManyField(
        Label,
        related_name='task_labels',
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
