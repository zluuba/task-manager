from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.urls import reverse_lazy

from task_manager.utils import AuthorizationCheckMixin, UserPermissionsMixin
from task_manager.tasks.models import Task

from .forms import UserCreateForm, UserUpdateForm, LoginForm
from .models import User


class UsersView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/users.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_message = _('You are logged in')

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(SuccessMessageMixin, LogoutView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')


class UserUpdateView(AuthorizationCheckMixin, UserPermissionsMixin,
                     SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')


class UserDeleteView(AuthorizationCheckMixin, UserPermissionsMixin,
                     SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')

    def form_valid(self, form):
        user_id = self.request.user.pk
        user_tasks = Task.objects.filter(author=user_id)

        if user_tasks:
            messages.error(
                self.request,
                _('Cannot delete a user because he is being used')
            )
            return redirect('users')
        return super().form_valid(form)
