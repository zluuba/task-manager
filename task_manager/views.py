from django.shortcuts import render, redirect
from django.views import View
from task_manager.users.forms import LoginForm


def index(request):
    title = 'Task manager'
    content = {
        'header': 'Hello there',
        'greetings': 'This is the Task Manager,',
        'body': 'I allow you to set tasks, assign performers and change their statuses. '
                'Registration and authentication are required to work with my system.',
    }
    return render(request, 'index.html', context={
        'title': title,
        'content': content,
    })


class LoginView(View):

    def get(self, request, *args, **kwargs):
        title = 'Sign In'
        form = LoginForm()
        return render(request, 'login.html', context={
            'title': title,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        title = 'Sign In'
        form = LoginForm()
        return render(request, 'login.html', context={
            'title': title,
            'form': form,
        })


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def page_not_found(request, exception):
    title = 'Page not found'
    content = {
        'sad_smile': '˙◠˙',
        'message': 'Page not found',
        'url_text': 'Go home'
    }
    return render(request, "page_not_found.html", context={
        'title': title,
        'content': content,
    })


def internal_server_error(request):
    title = 'Internal server error'
    content = {
        'sad_smile': '˙◠˙',
        'message': 'Internal server error',
        'url_text': 'Go home'
    }
    return render(request, "internal_server_error.html", context={
        'title': title,
        'content': content,
    })
