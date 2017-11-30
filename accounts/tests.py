from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class RegisterViewTest(TestCase):

    def test_page_loads(self):
        """ Проверяет загружается ли страница со статусом 200 (ОК) """
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template(self):
        """ Проверяет используется ли шаблон register.html """
        response = self.client.get('/register/')
        self.assertTemplateUsed(response, 'accounts/register.html')


class LoginViewTest(TestCase):

    def test_page_loads(self):
        """ Проверяет загружается ли страница со статусом 200 (ОК) """
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template(self):
        """ Проверяет используется ли шаблон login.html """
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'accounts/login.html')


class LoginTest(TestCase):
    
    def setUp(self):
        """ Подготовка к тестам: создание пользователя и клиента """
        self.credentials = {
            'phone': '+1234567890',
            'password': 'secret'
        }
        get_user_model().objects.create_user(**self.credentials)
    
    def test_user_exists(self):
        """ Проверяет создан ли пользователь """
        user = get_user_model().objects.get(phone = self.credentials['phone'])
        self.assertEqual(user.phone, self.credentials['phone'])

    def test_login(self):
        """ Проверяет аутентификацию """
        response = self.client.post('/login/', {
            'username': '+1234567890',
            'password': 'secret'
        }, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
