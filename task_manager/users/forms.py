from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


FIELD_STYLE = 'form-control bg-dark text-white'


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'label': 'Password',
            'class': FIELD_STYLE,
            'placeholder': 'Password',
        }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'label': 'Confirm password',
            'class': FIELD_STYLE,
            'placeholder': 'Confirm password',
        }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': FIELD_STYLE, 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': FIELD_STYLE, 'placeholder': 'Last name'}),
            'username': forms.TextInput(attrs={'class': FIELD_STYLE, 'placeholder': 'Username'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get("confirm_password")

        if len(password) <= 3:
            raise forms.ValidationError(
                "Password too short"
            )

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords doesn't match"
            )

        return password


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': FIELD_STYLE, 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': FIELD_STYLE, 'placeholder': 'Password'}),
        }
