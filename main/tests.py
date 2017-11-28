from django.test import TestCase, Client
from django.urls import reverse


class HomeViewTest(TestCase):

    def set_up(self):
        """ Подготовка к тестам: создание веб-клиента """
        self.client = Client()

    def test_page_loads(self):
        """ Проверяет загружается ли страница со статусом 200 (ОК) """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template(self):
        """ Проверяет используется ли шаблон home.html """
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home.html')
