from django.db import models
from task_manager.users.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.PROTECT)
    executor = models.ForeignKey(User, related_name='executor', null=True, blank=True, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, related_name='status', on_delete=models.PROTECT)
    labels = models.ManyToManyField(Label, related_name='labels', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
