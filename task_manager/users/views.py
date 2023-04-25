# from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView
from .forms import RegisterUserForm
from .models import User
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


class UsersView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'
    extra_context = {
        'title': _('Users'),
    }


class UserFormCreateView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    title = _('Sign Up')


class UserFormUpdateView(View):
    title = _('Edit profile')

    def get(self, request, *args, **kwargs):
        return render(request, 'users/update.html', context={
            'title': self.title,
        })

    def post(self, request, *args, **kwargs):
        return render(request, 'users/update.html', context={
            'title': self.title,
        })


class UserFormDeleteView(View):
    title = _('Delete account')

    def get(self, request, *args, **kwargs):
        return render(request, 'users/delete.html', context={
            'title': self.title,
        })

    def post(self, request, *args, **kwargs):
        return render(request, 'users/delete.html', context={
            'title': self.title,
        })
