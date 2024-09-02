from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        verbose_name=_('Name')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
