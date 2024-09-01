from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_('Title')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
