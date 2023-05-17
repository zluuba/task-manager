from django.contrib.auth.models import User as UserModel
from django.db import models


class User(UserModel):
    created_at = models.DateTimeField(auto_now_add=True)

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_fullname()
