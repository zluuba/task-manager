# from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import AddUserForm
from .models import User


FOOTER = {'text': 'by zluuba', 'url': 'https://github.com/zluuba'}


class IndexView(View):
    title = 'Users'

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        content = {
            'table_name': 'Users',
            'id': 'ID',
            'username': 'Username',
            'full_name': 'Full name',
            'created_at': 'Created at',
            'edit': 'Edit',
            'delete': 'Delete',
        }
        return render(request, 'users/users.html', context={
            'users': users,
            'title': self.title,
            'footer': FOOTER,
            'content': content,
        })


class UserFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = AddUserForm()
        return render(request, 'users/create.html', context={
            'form': form,
            'title': 'Sign Up',
            'footer': FOOTER,
        })

    def post(self, request, *args, **kwargs):
        form = AddUserForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                if password == form.cleaned_data['confirm_password']:
                    User.objects.create(first_name=first_name, last_name=last_name,
                                        username=username, password=password)
                messages.success(request, 'All done!')
                return redirect('home')
            except Exception as e:
                form.add_error(None, f'form: Cannot add user to db. Error: {e}')
                messages.error(request, f'Cannot add user to db. Error: {e}')
        else:
            messages.error(request, 'Fail. Form is not valid')
        return render(request, 'users/create.html', context={
            'form': form,
            'title': 'Sign In',
            'footer': FOOTER,
        })


class UserFormUpdateView(View):
    title = 'Edit profile'

    def get(self, request, *args, **kwargs):
        return render(request, 'users/update.html', context={
            'title': self.title,
            'footer': FOOTER,
        })

    def post(self, request, *args, **kwargs):
        return render(request, 'users/update.html', context={
            'title': self.title,
            'footer': FOOTER,
        })


class UserFormDeleteView(View):
    title = 'Delete account'

    def get(self, request, *args, **kwargs):
        return render(request, 'users/delete.html', context={
            'title': self.title,
            'footer': FOOTER,
        })

    def post(self, request, *args, **kwargs):
        return render(request, 'users/delete.html', context={
            'title': self.title,
            'footer': FOOTER,
        })
