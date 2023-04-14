from django.shortcuts import render
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
        return render(request, 'users/create.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'users/create.html')


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
