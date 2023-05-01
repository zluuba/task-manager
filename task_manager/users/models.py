from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User as Us
from django.db import models


class User(Us, AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_fullname()

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
