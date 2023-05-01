from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, UserChangeForm
)
from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username',
            'password1', 'password2',
        ]


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username',
        ]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'username', 'password1',
        ]
