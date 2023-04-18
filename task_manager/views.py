from django.shortcuts import render, redirect
from django.views import View


def index(request):
    return render(request, 'index.html')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'login.html')


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def page_not_found(request, exception):
    return render(request, "page_not_found.html")


def internal_server_error(request):
    return render(request, "internal_server_error.html")
