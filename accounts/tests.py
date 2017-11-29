from django.test import TestCase, Client
from django.urls import reverse


class RegisterViewTest(TestCase):

    def set_up(self):
        """ Подготовка к тестам: создание веб-клиента """
        self.client = Client()

    def test_page_loads(self):
        """ Проверяет загружается ли страница со статусом 200 (ОК) """
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template(self):
        """ Проверяет используется ли шаблон register.html """
        response = self.client.get('/register/')
        self.assertTemplateUsed(response, 'accounts/register.html')
