from django.test import TestCase, modify_settings
from django.contrib.messages import get_messages
from django.urls import reverse_lazy

from task_manager.users.models import User

from datetime import datetime


@modify_settings(
    MIDDLEWARE={'remove': [
        'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    ]}
)
class SetUpTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='Alice', last_name='Wang',
            username='alice_wang',
        )
        self.user.set_password('dfGt30jBY3')
        self.user.save()

        self.client.login(
            username='alice_wang', password='dfGt30jBY3',
        )


class UserCreateTestCase(SetUpTestCase):
    def test_user_creation(self):
        user = self.user

        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.first_name, 'Alice')
        self.assertEqual(str(user), 'Alice Wang')

        user_created_at = user.created_at.strftime('%Y-%m-%d')
        curr_time = datetime.now().strftime('%Y-%m-%d')
        self.assertEqual(user_created_at, curr_time)

    def test_user_registration_success(self):
        response = self.client.post(
            reverse_lazy('users_create'),
            {'first_name': 'Bob', 'last_name': 'Marks',
             'username': 'bob_marks', 'password1': 'gKlc89Cf1',
             'password2': 'gKlc89Cf1'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'User is successfully registered',
            'Пользователь успешно зарегистрирован',
        ])

    def test_user_registration_fail_username_already_exist(self):
        response = self.client.post(
            reverse_lazy('users_create'),
            {'first_name': 'Alice', 'last_name': 'Wang',
             'username': 'alice_wang', 'password1': 'dfGt30jBY3',
             'password2': 'dfGt30jBY3'}
        )
        self.assertEqual(response.status_code, 200)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 0)

    def test_user_registration_fail_passwords_not_match(self):
        response = self.client.post(
            reverse_lazy('users_create'),
            {'first_name': 'Alice', 'last_name': 'Wang',
             'username': 'alice_wang', 'password1': 'DFdfGt30jBY3',
             'password2': 'dfGt30jBY395'}
        )
        self.assertEqual(response.status_code, 200)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 0)

        curr_language = response.context['LANGUAGE_CODE']
        if curr_language == 'en-us':
            self.assertIn(
                'The two password fields didn’t match.',
                str(response.context['form'])
            )
        elif curr_language == 'ru-ru':
            self.assertIn(
                'Введенные пароли не совпадают.',
                str(response.context['form'])
            )


class UserUpdateTestCase(SetUpTestCase):
    def test_user_update_view(self):
        response = self.client.get(reverse_lazy('users_update',
                                                kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='form.html')

    def test_user_update_success(self):
        response = self.client.post(
            reverse_lazy('users_update', kwargs={'pk': 1}),
            {'first_name': 'Alice', 'last_name': 'Wang',
             'username': 'alice_wang_update', 'password1': 'dfGt30jBY3',
             'password2': 'dfGt30jBY3'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'User is successfully updated',
            'Пользователь успешно изменён',
        ])

    def test_user_update_no_permission(self):
        response = self.client.post(
            reverse_lazy('users_update', kwargs={'pk': 2}),
            {'first_name': 'Alice', 'last_name': 'Wang',
             'username': 'alice_wang_update', 'password1': 'dfGt30jBY3',
             'password2': 'dfGt30jBY3'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You have no rights to change another user.',
            'У вас нет прав для изменения другого пользователя.',
        ])

    def test_user_update_no_login(self):
        self.client.logout()

        response = self.client.get(
            reverse_lazy('users_update', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Вы не авторизованы! Пожалуйста, выполните вход.',
            'You are not logged in! Please log in.',
        ])


class UserDeleteTestCase(SetUpTestCase):
    def test_user_delete_view(self):
        response = self.client.get(reverse_lazy('users_delete',
                                                kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/delete.html')

    def test_user_delete_success(self):
        response = self.client.post(
            reverse_lazy('users_delete', kwargs={'pk': 1}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'User successfully deleted',
            'Пользователь успешно удалён',
        ])

    def test_user_delete_no_permission(self):
        response = self.client.post(
            reverse_lazy('users_delete', kwargs={'pk': 2}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You have no rights to change another user.',
            'У вас нет прав для изменения другого пользователя.',
        ])

    def test_user_delete_no_login(self):
        self.client.logout()

        response = self.client.get(
            reverse_lazy('users_delete', kwargs={'pk': 2}),
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Вы не авторизованы! Пожалуйста, выполните вход.',
            'You are not logged in! Please log in.',
        ])


class UserLoginTestCase(SetUpTestCase):
    def test_user_login_view(self):
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='form.html')

    def test_user_login_post(self):
        incorrect_login = self.client.login(
            username='incorrect_username', password='incorrect_password',
        )
        self.assertFalse(incorrect_login)

        response = self.client.post(
            reverse_lazy('login'),
            {"username": "alice_wang", "password": "dfGt30jBY3"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('home'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), ['You are logged in', 'Вы залогинены'])


class UsersListViewTestCase(SetUpTestCase):
    def test_users_list_view_not_login(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/users.html')

        curr_language = response.context['LANGUAGE_CODE']
        if curr_language == 'en-us':
            self.assertNotContains(response, 'Statuses')
            self.assertNotContains(response, 'Labels')
            self.assertNotContains(response, 'Tasks')
        else:
            self.assertNotContains(response, 'Статусы')
            self.assertNotContains(response, 'Метки')
            self.assertNotContains(response, 'Задачи')

    def test_users_list_view_login(self):
        response = self.client.get(reverse_lazy('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/users.html')

        curr_language = response.context['LANGUAGE_CODE']
        if curr_language == 'en-us':
            self.assertContains(response, 'Statuses')
            self.assertContains(response, 'Labels')
            self.assertContains(response, 'Tasks')
        else:
            self.assertContains(response, 'Статусы')
            self.assertContains(response, 'Метки')
            self.assertContains(response, 'Задачи')
