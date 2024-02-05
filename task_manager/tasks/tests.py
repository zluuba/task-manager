from django.test import TestCase, modify_settings
from django.contrib.messages import get_messages
from django.urls import reverse_lazy

from task_manager.users.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status

from .models import Task


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

        self.user2 = User.objects.create(
            first_name='Bob', last_name='Brown',
            username='bob_brown',
        )
        self.user2.set_password('hk70XhHG0D')
        self.user2.save()

        self.status = Status.objects.create(name='status')
        self.status.save()

        self.label = Label.objects.create(name='label')
        self.label.save()

        self.bob_task = Task.objects.create(
            name='bob_task', description='bob_task description',
            author=self.user2, status=self.status, executor=self.user2
        )
        self.bob_task.save()

        self.alice_task = Task.objects.create(
            name='alice_task', description='alice_task description',
            author=self.user, status=self.status, executor=self.user
        )
        self.alice_task.save()

        self.client.login(
            username='alice_wang', password='dfGt30jBY3',
        )


class TaskCreateTestCase(SetUpTestCase):
    def test_tasks_list_view(self):
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/tasks.html')

    def test_task_create_view(self):
        response = self.client.get(reverse_lazy('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/create.html')

    def test_task_create_success(self):
        response = self.client.post(
            reverse_lazy('task_create'),
            {'name': 'new_task', 'description': 'new_task description',
             'status': 1, 'executor': 1, 'labels': 1}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Task successfully created',
            'Задача успешно создана',
        ])

        new_task = Task.objects.get(name='new_task')
        self.assertIsNotNone(new_task)

    def test_task_create_fail_not_logged_in(self):
        self.client.logout()

        response = self.client.post(reverse_lazy('task_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You are not logged in! Please log in.',
            'Вы не авторизованы! Пожалуйста, выполните вход.',
        ])


class TaskUpdateTestCase(SetUpTestCase):
    def test_task_view(self):
        response = self.client.get(reverse_lazy(
            'task', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/task.html')

        task = Task.objects.get(pk=1)
        self.assertContains(response, task.name)
        self.assertContains(response, task.description)
        self.assertContains(response, task.status)
        self.assertContains(response, task.executor)

    def test_task_update_view(self):
        response = self.client.get(reverse_lazy(
            'task_update', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/update.html')

    def test_task_update_success(self):
        response = self.client.post(
            reverse_lazy('task_update', kwargs={'pk': 1}),
            {'name': 'task_updated', 'description': 'new_task description',
             'status': 1, 'executor': 1, 'labels': 1}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Task successfully updated',
            'Задача успешно изменена',
        ])

        updated_task = Task.objects.get(name='task_updated')
        self.assertIsNotNone(updated_task)

    def test_task_update_fail_not_logged_in(self):
        self.client.logout()

        response = self.client.post(reverse_lazy(
            'task_update', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You are not logged in! Please log in.',
            'Вы не авторизованы! Пожалуйста, выполните вход.',
        ])


class TaskDeleteTestCase(SetUpTestCase):
    def test_task_delete_view(self):
        response = self.client.get(reverse_lazy(
            'task_delete', kwargs={'pk': 2}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='tasks/delete.html')

    def test_task_delete_success(self):
        response = self.client.post(
            reverse_lazy('task_delete', kwargs={'pk': 2})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Task successfully deleted',
            'Задача успешно удалена',
        ])

        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=2)

    def test_task_delete_fail_user_not_author(self):
        response = self.client.post(
            reverse_lazy('task_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'The task can be deleted only by its author',
            'Задачу может удалить только её автор',
        ])

    def test_task_delete_fail_task_not_exist(self):
        response = self.client.post(
            reverse_lazy('task_delete', kwargs={'pk': 42})
        )
        self.assertEqual(response.status_code, 404)

    def test_task_delete_fail_not_logged_in(self):
        self.client.logout()

        response = self.client.post(reverse_lazy(
            'task_delete', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You are not logged in! Please log in.',
            'Вы не авторизованы! Пожалуйста, выполните вход.',
        ])
