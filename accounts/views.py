from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm
from .models import User


class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    model = User
    template_name = 'accounts/register.html'
