from django.test import TestCase, modify_settings
from django.contrib.messages import get_messages
from django.urls import reverse_lazy

from task_manager.users.models import User
from .models import Label


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

        self.label = Label.objects.create(name='label')
        self.label.save()


class LabelCreateTestCase(SetUpTestCase):
    def test_label_create_success(self):
        login = self.client.login(
            username='alice_wang', password='dfGt30jBY3',
        )
        self.assertTrue(login)

        response = self.client.post(
            reverse_lazy('label_create'),
            {'name': 'new_label'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Label successfully created',
            'Метка успешно создана',
        ])

        new_label = Label.objects.get(name='new_label')
        self.assertIsNotNone(new_label)

    def test_label_create_fail_not_logged_in(self):
        login = self.client.login()
        self.assertFalse(login)

        response = self.client.post(reverse_lazy('label_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You are not logged in! Please log in.',
            'Вы не авторизованы! Пожалуйста, выполните вход.',
        ])


class LabelUpdateTestCase(SetUpTestCase):
    def test_label_update_success(self):
        login = self.client.login(
            username='alice_wang', password='dfGt30jBY3',
        )
        self.assertTrue(login)

        response = self.client.post(
            reverse_lazy('label_update', kwargs={'pk': 1}),
            {'name': 'label_updated'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Label is successfully updated',
            'Метка успешно изменена',
        ])

        updated_label = Label.objects.get(name='label_updated')
        self.assertIsNotNone(updated_label)

    def test_label_update_fail_not_logged_in(self):
        login = self.client.login()
        self.assertFalse(login)

        response = self.client.post(reverse_lazy(
            'label_update', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You are not logged in! Please log in.',
            'Вы не авторизованы! Пожалуйста, выполните вход.',
        ])


class LabelDeleteTestCase(SetUpTestCase):
    def test_label_delete_success(self):
        login = self.client.login(
            username='alice_wang', password='dfGt30jBY3',
        )
        self.assertTrue(login)

        response = self.client.post(
            reverse_lazy('label_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'Label successfully deleted',
            'Метка успешно удалена',
        ])

        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(pk=1)

    def test_label_delete_fail_not_logged_in(self):
        login = self.client.login()
        self.assertFalse(login)

        response = self.client.post(reverse_lazy(
            'label_delete', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(str(messages[0]), [
            'You are not logged in! Please log in.',
            'Вы не авторизованы! Пожалуйста, выполните вход.',
        ])


class LabelViewsTestCase(SetUpTestCase):
    def test_labels_list_view(self):
        login = self.client.login(
            username='alice_wang', password='dfGt30jBY3',
        )
        self.assertTrue(login)
        response = self.client.get(reverse_lazy('labels'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='labels/labels.html')

    def test_label_create_view(self):
        login = self.client.login(
            username='alice_wang', password='dfGt30jBY3',
        )
        self.assertTrue(login)
        response = self.client.get(reverse_lazy('label_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='labels/form.html')

    def test_label_update_view(self):
        login = self.client.login(
            username='alice_wang', password='dfGt30jBY3',
        )
        self.assertTrue(login)
        response = self.client.get(reverse_lazy(
            'label_update', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='labels/form.html')

    def test_label_delete_view(self):
        login = self.client.login(
            username='alice_wang', password='dfGt30jBY3',
        )
        self.assertTrue(login)
        response = self.client.get(reverse_lazy(
            'label_delete', kwargs={'pk': 1}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='labels/delete.html')
