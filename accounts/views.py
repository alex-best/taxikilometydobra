from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegistrationForm, AccountChangeForm
from .models import User


class RegistrationView(CreateView):
    """ Страница содержащая форму регистрации """

    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    model = User
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        """ Перенаправить пользователя на главную страницу, если он уже вошел в систему """
        
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return super().dispatch(request, *args, **kwargs)


class ChangeAccountView(LoginRequiredMixin, FormView):
    """ Страница содержащая форму смены информации """

    login_url = '/login/'
    redirect_field_name = 'redirect'
    form_class = AccountChangeForm
    template_name = 'settings/settings-account.html'
    success_url = reverse_lazy('settings-account')

    def get_form(self):
        return self.form_class(instance=self.request.user, **self.get_form_kwargs())

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Данные учётной записи изменены!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Пожалуйста, проверьте введённые данные!')
        return self.render_to_response(self.get_context_data(form=form))


class ChangePasswordView(LoginRequiredMixin, FormView):
    """ Страница содержащая форму смены пароля """

    login_url = '/login/'
    redirect_field_name = 'redirect'
    form_class = PasswordChangeForm
    template_name = 'settings/settings-password.html'
    success_url = reverse_lazy('settings-password')

    def get_form(self):
        return self.form_class(self.request.user, **self.get_form_kwargs())

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, 'Ваш пароль был успешно обновлён!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Пожалуйста, проверьте введённые данные!')
        return self.render_to_response(self.get_context_data(form=form))
