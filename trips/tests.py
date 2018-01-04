from django.test import TestCase
import datetime
from django.contrib.auth import get_user_model

from .forms import CreateTripForm
from .models import Trip


class TripsListTest(TestCase):

    def setUp(self):
        self.existing_user = {'phone': '+321654789', 'password': 'supersecretpass123'}
        self.user = get_user_model().objects.create_user(**self.existing_user)
        self.client.login(**self.existing_user)

    def test_page_loads_200(self):
        response = self.client.get('/trips/list')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template_trips_list(self):
        response = self.client.get('/trips/list')
        self.assertTemplateUsed(response, 'trips/trips-list.html')


class CreateTripViewTest(TestCase):

    def setUp(self):
        self.existing_user = {'phone': '+321654789', 'password': 'supersecretpass123'}
        self.user = get_user_model().objects.create_user(**self.existing_user)
        self.client.login(**self.existing_user)

    def test_page_loads_200(self):
        response = self.client.get('/trips/create')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template_trips_list(self):
        response = self.client.get('/trips/create')
        self.assertTemplateUsed(response, 'trips/trips-create.html')


class CreateTripFormTest(TestCase):

    def setUp(self):
        self.existing_user = {'phone': '+321654789', 'password': 'supersecretpass123'}
        self.user = get_user_model().objects.create_user(**self.existing_user)
        self.client.login(**self.existing_user)
    
    def test_form_valid_data_true(self):
        form = CreateTripForm(data={'departure': 'Солнечный город', 'arrival': 'Луна', 'purpose': 'Полёт',
        'date': '2015-03-11', 'departure_time': '00:16:31.000099', 'arrival_time': '00:16:31.000099'})
        self.assertTrue(form.is_valid())

    def test_form_departure_empty_false(self):
        form = CreateTripForm(data={'departure': '', 'arrival': 'Луна', 'purpose': 'Полёт',
        'date': '2015-03-11', 'departure_time': '00:16:31.000099', 'arrival_time': '00:16:31.000099'})
        self.assertFalse(form.is_valid())
    
    def test_form_arrival_empty_false(self):
        form = CreateTripForm(data={'departure': 'Солнечный город', 'arrival': '', 'purpose': 'Полёт',
        'date': '2015-03-11', 'departure_time': '00:16:31.000099', 'arrival_time': '00:16:31.000099'})
        self.assertFalse(form.is_valid())

    def test_form_purpose_empty_false(self):
        form = CreateTripForm(data={'departure': 'Солнечный город', 'arrival': 'Луна', 'purpose': '',
        'date': '2015-03-11', 'departure_time': '00:16:31.000099', 'arrival_time': '00:16:31.000099'})
        self.assertFalse(form.is_valid())
    
    def test_form_date_empty_false(self):
        form = CreateTripForm(data={'departure': 'Солнечный город', 'arrival': 'Луна', 'purpose': 'Полёт',
        'date': '', 'departure_time': '00:16:31.000099', 'arrival_time': '00:16:31.000099'})
        self.assertFalse(form.is_valid())

    def test_form_departure_time_empty_false(self):
        form = CreateTripForm(data={'departure': 'Солнечный город', 'arrival': 'Луна', 'purpose': 'Полёт',
        'date': '2015-03-11', 'departure_time': '', 'arrival_time': '00:16:31.000099'})
        self.assertFalse(form.is_valid())

    def test_form_arrival_time_empty_true(self):
        form = CreateTripForm(data={'departure': 'Солнечный город', 'arrival': 'Луна', 'purpose': 'Полёт',
        'date': '2015-03-11', 'departure_time': '00:16:31.000099', 'arrival_time': ''})
        self.assertTrue(form.is_valid())

    def test_form_time_invalid_false(self):
        form = CreateTripForm(data={'departure': 'Солнечный город', 'arrival': 'Луна', 'purpose': 'Полёт',
        'date': '2015-03-11', 'departure_time': '123', 'arrival_time': 'abc'})
        self.assertFalse(form.is_valid())
    
    def test_form_date_invalid_false(self):
        form = CreateTripForm(data={'departure': 'Солнечный город', 'arrival': 'Луна', 'purpose': 'Полёт',
        'date': '5-5-5', 'departure_time': '00:16:31.000099', 'arrival_time': '00:16:31.000099'})
        self.assertFalse(form.is_valid())


class TripCreationTest(TestCase):
    
    def test_trip_creation(self):
        user_data = {'phone': '+321654789', 'password': 'supersecretpass123'}

        # Пользователь заходит на главную страницу
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

        # Переходит на страницу регистрации
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

        # Заполняет форму и жмёт на кнопку подтверждения
        response = self.client.post('/register/', data=user_data)
        self.assertEqual(response.status_code, 302)

        # Переходит на страницу логина
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

        # Вводит данные и жмет Войти
        response = self.client.post('/login/', 
        {'username': '+321654789', 'password': 'supersecretpass123'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.client.login(**user_data)

        # Переходит на вкладку создания новой поездки
        response = self.client.get('/trips/create')
        self.assertEqual(response.status_code, 200)

        # Заполняет данные и подтверждает форму
        response = self.client.post('/trips/create', data={'departure': 'Солнечный город', 'arrival': 'Луна', 'purpose': 'Полёт',
        'date': '2015-03-11', 'departure_time': '00:16:31.000099', 'arrival_time': '00:16:31.000099'})
        self.assertEqual(response.status_code, 302)

