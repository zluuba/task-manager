from django.test import TestCase
from django.urls import reverse_lazy


class HomeViewTestCase(TestCase):
    def test_home(self):
        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='home.html')
