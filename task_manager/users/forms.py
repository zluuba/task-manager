from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User

from task_manager.utils import get_form_fields

FIELDS = get_form_fields()


class UserCreateForm(UserCreationForm):
    """
    Do something with fields.
    Get rid of get_form_fields func
    """
    first_name, last_name, username, \
        password1, password2 = [field for field in FIELDS.values()]

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username',
            'password1', 'password2',
        ]


class UserUpdateForm(UserChangeForm):
    first_name, last_name, username, \
        password1, password2 = [field for field in FIELDS.values()]

    password = None

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username',
        ]


class LoginForm(AuthenticationForm):
    fields = get_form_fields(help_text=False)
    username = fields['username']
    password = fields['password1']
