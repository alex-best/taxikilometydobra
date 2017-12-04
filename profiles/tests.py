from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import FamilyProfile


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

    def test_user_profile_created(self):
        """ Проверяет создаётся ли профиль для нового пользователя (не администратора) """
        self.assertIsNotNone(FamilyProfile.objects.get(user = self.user))

    def test_profile_created(self):
        """ Проверяет создаётся ли профиль для нового пользователя (администратора) """
        with self.assertRaises(FamilyProfile.DoesNotExist):
            FamilyProfile.objects.get(user = self.superuser)
