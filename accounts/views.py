from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegistrationForm, AccountChangeForm


class RegistrationView(FormView):
    """Страница регистрации
    
    Страница содержит форму для регистрации нового пользователя. 
    После успешной регистрации пользователь аутентифицируется 
    и перенаправляется на страницу редактирования профиля.

    Связанные требования: R 2.1 - R 2.10
    """

    form_class = RegistrationForm
    success_url = reverse_lazy('settings-profile')
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        """Форма валидна

        Сохраняем пользователя, аутентифицируем и перенаправляем 
        в настройки профиля.
        """

        user = form.save()
        user.profile.user_type = form.cleaned_data.get('user_type')
        user.profile.save()
        authenticate(
            phone=form.cleaned_data.get('phone'), 
            password=form.cleaned_data.get('password')
        )
        login(self.request, user)
        return redirect('settings-profile')


class ChangeAccountView(LoginRequiredMixin, FormView):
    """Страница изменения информации учётной записи
    
    Страница содержит форму для изменения основных полей учётной 
    записи (исключая пароль).

    Связанные требования: R 4.3.2 - R 4.3.6
    """

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
    """Страница изменения пароля учётной записи
    
    Страница содержит форму для изменения пароля учётной записи.

    Связанные требования: 4.4.1 - 4.4.6
    """

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
