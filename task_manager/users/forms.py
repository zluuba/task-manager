from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, UserChangeForm
)
from django.utils.translation import gettext as _
from django import forms

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

    password1 = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=_('Confirm password'),
        widget=forms.PasswordInput
    )

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
