from django.forms import ModelForm
from django.forms.widgets import TextInput, NumberInput, Textarea

from .models import FamilyProfile


class FamilyProfileChangeForm(ModelForm):
    class Meta:
        model = FamilyProfile
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