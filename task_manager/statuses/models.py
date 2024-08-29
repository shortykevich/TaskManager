from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # tasks = models.ManyToManyField(
    #     'Task',
    #     related_name='statuses',
    #     on_delete=models.CASCADE
    # )

    def __str__(self):
        return self.title
