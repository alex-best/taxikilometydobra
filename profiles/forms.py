from django.forms import ModelForm
from django.forms.widgets import TextInput, NumberInput, Textarea

from .models import Profile


class FamilyProfileForm(ModelForm):
    """Форма для редактирования профиля

    Форма позволяет изменять профиль пользователя
    в зависимости от его типа.
    """
    class Meta:
        model = Profile
        fields = ['trips_per_month', 'car_requirements', 'info']
        widgets = {
            'trips_per_month': NumberInput( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Необходимое количество поездок в месяц',
                }
            ),
            'car_requirements': Textarea( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Требования к машине',
                    'rows': 3,
                }
            ),
            'info': Textarea( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Дополнительная информация',
                    'rows': 5,
                }
            ),
        }


class BenefactorProfileForm(ModelForm):
    """Форма для редактирования профиля

    Форма позволяет изменять профиль пользователя
    в зависимости от его типа.
    """
    class Meta:
        model = Profile
        fields = ['about', ]
        widgets = {
            'about': Textarea( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'О себе',
                    'rows': 5,
                }
            ),
        }


class StaffProfileForm(ModelForm):
    """Форма для редактирования профиля

    Форма позволяет изменять профиль пользователя
    в зависимости от его типа.
    """
    class Meta:
        model = Profile
        fields = ['position', ]
        widgets = {
            'position': TextInput( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Позиция',
                }
            ),
        }