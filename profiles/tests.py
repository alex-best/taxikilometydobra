from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import FamilyProfile


class ProfileModelTest(TestCase):

    def setUp(self):
        """ Подготовка к тестам: создание пользователя """
        self.credentials = {
            'phone': '+1234567890',
            'password': 'secret'
        }
        get_user_model().objects.create_user(**self.credentials)

    def test_profile_created(self):
        """ Проверяет создаётся ли профиль для каждого нового пользователя """
        user = get_user_model().objects.get(phone = self.credentials['phone'])
        self.assertIsNotNone(user.profile)
