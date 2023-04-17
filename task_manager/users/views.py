from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import User


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Создан аккаунт {username}!')
            return render(request, 'index.html')
        else:
            messages.success(request, 'Fail')
        return render(request, 'users/create.html', {'form': form})


class UserFormUpdateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/update.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'users/update.html')


class UserFormDeleteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/delete.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'users/delete.html')
