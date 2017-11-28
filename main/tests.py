from django.test import TestCase, Client
from django.urls import reverse


class HomeViewTest(TestCase):

    def set_up(self):
        self.client = Client()

    def test_page_loads(self):
        """ Is page loaded with 200 (OK) and 'home.html' template? """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
