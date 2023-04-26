from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy

from .forms import UserForm, LoginForm
from .models import User


class UsersView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/users.html'
    extra_context = {
        'title': _('Users'),                                    # ru: "Пользователи"
        'fields': ['ID', _('Username'), _('Full name'),         # ru: "Имя пользователя", "Полное имя"
                   _('Created at'), ''],                        # ru: "Дата создания"
        'edit_btn': _('Edit'),                                  # ru: "Изменить"
        'delete_btn': _('Delete'),                              # ru: "Удалить"
    }


class UserCreateView(CreateView):
    """
    Create auto-login after all

        def form-valid(self, form):
            user = form.save()
            login(self.request, user)
            return redirect('home')
    """

    form_class = UserForm
    template_name = 'users/form.html'
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')      # ru: "Пользователь успешно зарегистрирован"
    extra_context = {
        'title': _('Sign up'),                                  # ru: "Регистрация"
        'button': _('Sign up'),                                 # ru: "Зарегистрировать"
    }


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = 'users/form.html'
    success_message = _('You are logged in')                    # ru: "Вы залогинены"
    extra_context = {
        'title': _('Sign in'),                                  # ru: "Вход"
        'button': _('Sign in'),                                 # ru: "Войти"
    }

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogout(View):
    def get(self, request):
        logout(request)
        messages.info(request, _('You are logged out'))         # ru msg: "Вы разлогинены"
        return redirect('home')


class UserUpdateView(UpdateView):
    """
    if choosing user not curr user:
        if user logged in:
            - show "You have no rights to change another user."
                (ru: "У вас нет прав для изменения другого пользователя.")
        else:
            - show "You are not logged in! Please log in."
                (ru: "Вы не авторизованы! Пожалуйста, выполните вход.")
            - redirect to 'login'
    """

    model = User
    form_class = UserForm
    template_name = 'users/form.html'
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')         # ru: "Пользователь успешно изменён"
    extra_context = {
        'title': _('Update user'),                              # ru: "Изменить пользователя"
        'button': _('Update'),                                  # ru: "Изменить"
    }


class UserDeleteView(SuccessMessageMixin, DeleteView):
    """
    if user have active task:
        - do not delete user
        - show "Cannot delete a user because he is being used" - red
            (ru: "Невозможно удалить пользователя, потому что он используется")
        - redirect to 'users'

    if choosing user not curr user:
        if user logged in:
            - show "You have no rights to change another user." - red
                (ru: "У вас нет прав для изменения другого пользователя.")
        else:
            - show "You are not logged in! Please log in." - red
                (ru: "Вы не авторизованы! Пожалуйста, выполните вход.")
            - redirect to 'login'
    """

    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')            # ru: "Пользователь успешно удалён"
    extra_context = {
        'title': _('Delete user'),                              # ru: "Удалить пользователя"
        'text': _('Are you sure you want to delete '),          # ru: "Вы уверены, что хотите удалить "
        'button': _('Yes, delete'),                             # ru: "Да, удалить"
    }
