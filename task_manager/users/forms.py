from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _
from django import forms
from .models import User


CLASS_WID = {'class': 'form-control bg-dark text-white'}


class UserForm(UserCreationForm):
    """
    Change the form - should be smaller (+ don't double LoginForm)
    Add clear method (?)
    """

    first_name = forms.CharField(
        label=_('First name'),
        widget=forms.TextInput(attrs=CLASS_WID))
    last_name = forms.CharField(
        label=_('Last name'),
        widget=forms.TextInput(attrs=CLASS_WID))
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs=CLASS_WID))

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs=CLASS_WID))
    password2 = forms.CharField(
        label=_('Confirm password'),
        widget=forms.PasswordInput(attrs=CLASS_WID))

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username',
            'password1', 'password2'
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs=CLASS_WID))
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs=CLASS_WID))
