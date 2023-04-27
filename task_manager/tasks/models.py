from django.db import models
from task_manager.users.models import User
# from django.conf import settings
# from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    # performer = models.ForeignKey(User, on_delete=models.PROTECT)
    # status = models.ForeignKey(Status, on_delete=models.models.PROTECT)
    # labels = models.ManyToManyField(Status, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
