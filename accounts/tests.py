from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import RegistrationForm, AccountChangeForm

class RegisterViewTest(TestCase):

    def test_page_loads_200(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template_register(self):
        response = self.client.get('/register/')
        self.assertTemplateUsed(response, 'accounts/register.html')


class LoginViewTest(TestCase):

    def test_page_loads_200(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'accounts/login.html')


class ChangeAccountViewTest(TestCase):

    def setUp(self):
        self.existing_user = {'phone': '+321654789', 'password': 'supersecretpass123'}
        get_user_model().objects.create_user(**self.existing_user)
        self.client.login(**self.existing_user)

    def test_page_loads_200(self):
        response = self.client.get('/settings/account')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template(self):
        response = self.client.get('/settings/account')
        self.assertTemplateUsed(response, 'settings/settings-account.html')


class ChangePasswordViewTest(TestCase):

    def setUp(self):
        self.existing_user = {'phone': '+321654789', 'password': 'supersecretpass123'}
        get_user_model().objects.create_user(**self.existing_user)
        self.client.login(**self.existing_user)

    def test_page_loads_200(self):
        response = self.client.get('/settings/password')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template(self):
        response = self.client.get('/settings/password')
        self.assertTemplateUsed(response, 'settings/settings-password.html')


class RegisterFormTest(TestCase):

    def setUp(self):
        self.valid_data = data = {'phone': '+123456789', 'password': 'supersecretpass123'}
        self.existing_user = {'phone': '+321654789', 'password': 'supersecretpass123'}
        get_user_model().objects.create_user(**self.existing_user)
    
    def test_form_valid_data_true(self):
        form = RegistrationForm(data={'phone': '+123456789', 'password': 'supersecretpass123'})
        self.assertTrue(form.is_valid())
    
    def test_form_valid_fulldata_true(self):
        form = RegistrationForm(data={'phone': '+123456789', 'password': 'supersecretpass123',
        'first_name': 'Ivan', 'last_name': 'Ivanov'})
        self.assertTrue(form.is_valid())

    def test_form_existing_user_false(self):
        form = RegistrationForm(data=self.existing_user)
        self.assertFalse(form.is_valid())

    def test_form_invalid_phone_false(self):
        form = RegistrationForm(data={'phone': '+123', 'password': 'supersecretpass123'})
        self.assertFalse(form.is_valid())

    def test_form_invalid_password_false(self):
        form = RegistrationForm(data={'phone': '+123456789', 'password': '123'})
        self.assertFalse(form.is_valid())
    
    def test_form_password_empty_false(self):
        form = RegistrationForm(data={'phone':'+123456789', 'password': ''})
        self.assertFalse(form.is_valid())
    
    def test_form_phone_empty_false(self):
        form = RegistrationForm(data={'phone':'', 'password': 'supersecretpass123'})
        self.assertFalse(form.is_valid())
    
    def test_form_valid_creates_user_true(self):
        form = RegistrationForm(data=self.valid_data)
        form.save()
        self.assertIsNotNone(get_user_model().objects.get(phone=self.valid_data['phone']))


class LoginFormTest(TestCase):
    
    def setUp(self):
        self.credentials = {
            'phone': '+1234567890',
            'password': 'secret'
        }
        get_user_model().objects.create_user(**self.credentials)
    
    def test_user_exists(self):
        user = get_user_model().objects.get(phone = self.credentials['phone'])
        self.assertEqual(user.phone, self.credentials['phone'])

    def test_login_valid_true(self):
        response = self.client.post('/login/', 
        {'username': '+1234567890', 'password': 'secret'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
    
    def test_login_password_invalid_false(self):
        response = self.client.post('/login/', 
        {'username': '+1234567890', 'password': 'invalid'}, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
    
    def test_login_password_empty_false(self):
        response = self.client.post('/login/', 
        {'username': '+1234567890', 'password': ''}, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
    
    def test_login_username_invalid_false(self):
        response = self.client.post('/login/', 
        {'username': '+123', 'password': 'secret'}, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
    
    def test_login_username_empty_false(self):
        response = self.client.post('/login/', 
        {'username': '', 'password': 'secret'}, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)


class AccountChangeFormTest(TestCase):
    
    def setUp(self):
        self.existing_user = {'phone': '+321654789', 'password': 'supersecretpass123'}
        self.user = get_user_model().objects.create_user(**self.existing_user)
        self.client.login(**self.existing_user)
    
    def test_form_valid_data_true(self):
        form = AccountChangeForm(instance=self.user, data={'phone': '+321654789'})
        self.assertTrue(form.is_valid())

    def test_form_valid_fulldata_true(self):
        form = AccountChangeForm(instance=self.user, data={'phone': '+321654789', 
        'first_name': 'Ivan', 'last_name': 'Ivanov'})
        self.assertTrue(form.is_valid())
    
    def test_form_phone_valid_true(self):
        form = AccountChangeForm(instance=self.user, data={'phone': '+321654780'})
        self.assertTrue(form.is_valid())

    def test_form_phone_empty_false(self):
        form = AccountChangeForm(instance=self.user, data={'phone': ''})
        self.assertFalse(form.is_valid())

    def test_form_phone_invalid_false(self):
        form = AccountChangeForm(instance=self.user, data={'phone': '+123'})
        self.assertFalse(form.is_valid())

    def test_form_data_empty_true(self):
        form = AccountChangeForm(instance=self.user, data={'phone': '+321654789', 
        'first_name': '', 'last_name': ''})
        self.assertTrue(form.is_valid())

