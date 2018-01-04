from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Profile, UserTypes
from .views import ChangeProfileView
from .forms import BenefactorProfileForm


class ChangeProfileViewTest(TestCase):

    def setUp(self):
        self.existing_user = {'phone': '+321654789', 'password': 'supersecretpass123'}
        self.user = get_user_model().objects.create_user(**self.existing_user)
        self.client.login(**self.existing_user)

    def test_page_loads_200(self):
        response = self.client.get('/settings/profile')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template_register(self):
        response = self.client.get('/settings/profile')
        self.assertTemplateUsed(response, 'settings/settings-profile.html')


class ProfileDetailTest(TestCase):

    def setUp(self):
        self.existing_user = {'phone': '+321654789', 'password': 'supersecretpass123'}
        get_user_model().objects.create_user(**self.existing_user)
        self.client.login(**self.existing_user)

    def test_page_loads_200(self):
        response = self.client.get('/me')
        self.assertEqual(response.status_code, 200)
    
    def test_page_template_register(self):
        response = self.client.get('/me')
        self.assertTemplateUsed(response, 'profiles/profile-details.html')


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user_credentials = {'phone': '+1234567890', 'password': 'secret'}
        self.user = get_user_model().objects.create_user(**self.user_credentials)

    def test_profile_created_true(self):
        self.assertIsNotNone(Profile.objects.get(user = self.user))

    def test_profile_default_type_true(self):
        self.assertEqual(Profile.objects.get(user = self.user).user_type, UserTypes.BENEFACTOR)

