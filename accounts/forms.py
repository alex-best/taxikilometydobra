from django import forms
from django.forms.widgets import PasswordInput, TextInput, RadioSelect
from django.contrib.auth.password_validation import validate_password

from profiles.models import UserTypes

from .models import User


class RegistrationForm(forms.ModelForm):
    """Форма регистрации
    
    Форма используется для создания новой учётной записи 
    пользователя.

    Связанные требования: R 2.2 - R 2.10
    """

    user_type = forms.ChoiceField(
        required = True,
        choices=UserTypes.CHOICES[1:], 
        widget=RadioSelect(attrs={'class':'uk-radio'}),
        initial=UserTypes.CHOICES[1][0],
    )
    error_css_class = 'uk-form-danger'

    def clean_password(self):
        """Проверка сложности пароля

        Пароль проходит все валидаторы из настройки 
        AUTH_PASSWORD_VALIDATORS. Вызывает ValidationError.
        """
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password

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
    """Форма редактирования учётной записи
    
    Форма используется для редактирования существующей учётной 
    записи пользователя. Содержит телефон, имя и фамилию.

    Связанные требования: R 4.3.2 - R 4.3.6
    """

    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name']