from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
