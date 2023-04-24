from django import forms
from .models import User


FIELD_STYLE = 'form-control bg-dark text-white'


class AddUserForm(forms.Form):
    first_name = forms.CharField(max_length=255, label='First name',
                                 widget=forms.TextInput(attrs={
                                     'class': FIELD_STYLE,
                                     'placeholder': 'First name'
                                 }))
    last_name = forms.CharField(max_length=255, label='Last name',
                                widget=forms.TextInput(attrs={
                                    'class': FIELD_STYLE,
                                    'placeholder': 'Last name',
                                }))
    username = forms.CharField(max_length=255, label='Username',
                               widget=forms.TextInput(attrs={
                                   'class': FIELD_STYLE,
                                   'placeholder': 'Username',
                               }))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                   'class': FIELD_STYLE,
                                   'placeholder': 'Password',
                               }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                                    'class': FIELD_STYLE,
                                    'placeholder': 'Confirm password',
                               }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

    def clean(self):
        cleaned_data = super(AddUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords doesn't match"
            )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Username',
                               widget=forms.TextInput(attrs={
                                   'class': FIELD_STYLE,
                                   'placeholder': 'Username',
                               }))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                   'class': FIELD_STYLE,
                                   'placeholder': 'Password',
                               }))
