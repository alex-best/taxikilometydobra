from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import RegistrationForm
from .models import User


class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = '/login/'
    model = User
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.get_success_url())