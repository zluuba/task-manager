from django.db.models.deletion import ProtectedError
from django.test import TestCase, modify_settings
from django.contrib.messages import get_messages
from django.urls import reverse_lazy

from task_manager.users.models import User
from task_manager.tasks.models import Task
from .models import Status


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

        self.status = Status.objects.create(name='status')
        self.status.save()

        self.status2 = Status.objects.create(name='status2')
        self.status2.save()

        self.task = Task.objects.create(
            name='task', description='task description',
            author=self.user, status=self.status2, executor=self.user
        )
        self.task.save()

        self.client.login(
            username='alice_wang', password='dfGt30jBY3',
        )


class StatusCreateTestCase(SetUpTestCase):
    def test_status_create_success(self):
        response = self.client.post(
            reverse_lazy('status_create'),
            {'name': 'new_status'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Status successfully created',
            'Статус успешно создан',
        ])
        new_status = Status.objects.get(name='new_status')
        self.assertIsNotNone(new_status)

    def test_status_create_fail_not_logged_in(self):
        self.client.logout()

        response = self.client.post(reverse_lazy('status_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You are not logged in! Please log in.',
            'Вы не авторизованы! Пожалуйста, выполните вход.',
        ])


class StatusUpdateTestCase(SetUpTestCase):
    def test_status_update_success(self):
        response = self.client.post(
            reverse_lazy('status_update', kwargs={'pk': 1}),
            {'name': 'status_updated'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Status is successfully updated',
            'Статус успешно изменён',
        ])

        updated_status = Status.objects.get(name='status_updated')
        self.assertIsNotNone(updated_status)

    def test_status_update_fail_not_logged_in(self):
        self.client.logout()

        response = self.client.post(reverse_lazy(
            'status_update', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You are not logged in! Please log in.',
            'Вы не авторизованы! Пожалуйста, выполните вход.',
        ])


class StatusDeleteTestCase(SetUpTestCase):
    def test_status_delete_success(self):
        response = self.client.post(
            reverse_lazy('status_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Status successfully deleted',
            'Статус успешно удалён',
        ])

        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(pk=1)

    def test_status_delete_fail_used_by_task(self):
        with self.assertRaises(ProtectedError):
            self.client.post(reverse_lazy(
                'status_delete', kwargs={'pk': 2}
            ))

    def test_status_delete_fail_not_logged_in(self):
        self.client.logout()

        response = self.client.post(reverse_lazy(
            'status_delete', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You are not logged in! Please log in.',
            'Вы не авторизованы! Пожалуйста, выполните вход.',
        ])


class StatusViewsTestCase(SetUpTestCase):
    def test_statuses_list_view(self):
        response = self.client.get(reverse_lazy('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='statuses/statuses.html'
        )

    def test_status_create_view(self):
        response = self.client.get(reverse_lazy('status_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuses/form.html')

    def test_status_update_view(self):
        response = self.client.get(reverse_lazy(
            'status_update', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuses/form.html')

    def test_status_delete_view(self):
        response = self.client.get(reverse_lazy(
            'status_delete', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuses/delete.html')
