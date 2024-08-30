from django.db import models

from task_manager.statuses.models import Status
from task_manager.users.models import User


# class Task(models.Model):
#     author = models.ForeignKey(User, on_delete=models.PROTECT)
#     status = models.ForeignKey(Status, on_delete=models.PROTECT)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     # lables = models.ManyToManyField()
#
#     def __str__(self):
#         return self.title
