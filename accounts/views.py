from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm
from .models import User


class RegistrationView(CreateView):
    """ Страница содержащая форму регистрации """

    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    model = User
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        """ Перенаправить пользователя на главную страницу, если он уже вошел в систем """
        
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return super().dispatch(request, *args, **kwargs)
