from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

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

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
