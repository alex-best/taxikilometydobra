from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import User


class RegistrationForm(forms.ModelForm):
    """ Форма для создания новой учётной записи пользователя """

    error_css_class = 'uk-form-danger'

    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'password']
        help_texts = {
            'phone': 'Пожалуйста, укажите свой настоящий телефон, чтобы мы могли с вами связаться.',
        }
        error_messages = {
            'phone': {
                'unique': 'Пользователь с таким телефоном уже существует!',
                'max_length': "Телефон слишком длинный, проверьте правильность введенных данных.",
            },
        }
        widgets = {
            'phone': forms.TextInput( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Телефон',
                    'type': 'tel',
                }
            ),
            'first_name': forms.TextInput( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Имя',
                }
            ),
            'last_name': forms.TextInput( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Фамилия',
                }
            ),
            'password': forms.PasswordInput( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Пароль',
                }
            ),
        }

class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name']