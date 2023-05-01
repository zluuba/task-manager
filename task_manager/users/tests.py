from django.test import TestCase, modify_settings
from django.urls import reverse_lazy

from task_manager.users.models import User
from datetime import datetime


class SetUpTestCase(TestCase):
    def setUp(self):
        self.alice = User.objects.create(
            first_name='Alice', last_name='Wang',
            username='alice_wang'
        )


class UserCreateTestCase(SetUpTestCase):
    def test_user_creation(self):
        alice = User.objects.get(username='alice_wang')

        self.assertTrue(isinstance(alice, User))
        self.assertEqual(alice.first_name, 'Alice')
        self.assertEqual(alice.get_fullname(), 'Alice Wang')

        alice_created_at = alice.created_at.strftime('%Y-%m-%d')
        curr_time = datetime.now().strftime('%Y-%m-%d')
        self.assertEqual(alice_created_at, curr_time)


class UserViewsTestCase(SetUpTestCase):
    @modify_settings(
        MIDDLEWARE={'remove': [
            'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
        ]}
    )
    def test_user_views(self):
        # login
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/form.html')
        # users list
        response = self.client.get(reverse_lazy('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/users.html')
        # user creation
        response = self.client.get(reverse_lazy('users_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/form.html')
        # user modification
        response = self.client.get(reverse_lazy('users_update',
                                                kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
        # user deletion
        response = self.client.get(reverse_lazy('users_delete',
                                                kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users'))
