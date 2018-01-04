from django.test import TestCase, Client
from django.urls import reverse


class HomeViewTest(TestCase):

    def test_page_loads_200(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template_home(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home.html')
