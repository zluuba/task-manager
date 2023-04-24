# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User as Us
from django.db import models
# from django import forms


# class User(AbstractUser):
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)

class User(models.Model):
    first_name = models.CharField(max_length=150)   # verbose_name
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
