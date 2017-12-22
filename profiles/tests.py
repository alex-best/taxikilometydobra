from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Profile, UserTypes


class ProfileModelTest(TestCase):

    def setUp(self):
        """ Подготовка к тестам: создание пользователя """
        self.user_credentials = {
            'phone': '+1234567890',
            'password': 'secret'
        }
        self.superuser_credentials = {
            'phone': '+0987654321',
            'password': 'supersecret'
        }
        self.user = get_user_model().objects.create_user(**self.user_credentials)
        self.superuser = get_user_model().objects.create_superuser(**self.superuser_credentials)

