from django.forms import ModelForm
from django.forms.widgets import TextInput, NumberInput, Textarea, DateInput, TimeInput

from .models import Trip


class CreateTripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['departure', 'arrival', 'purpose', 'date', 'departure_time', 'arrival_time']
        widgets = {
            'departure': TextInput( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Цветочный город',
                }
            ),
            'arrival': TextInput( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Солнечный город',
                }
            ),
            'purpose': TextInput( attrs = {
                    'class': 'uk-input',
                    'placeholder': 'Путешествие с Кнопочкой',
                }
            ),
            'date': DateInput( attrs = {
                    'class': 'uk-input',
                    'type': 'date',
                }
            ),
            'departure_time': TimeInput( attrs = {
                    'class': 'uk-input',
                    'type': 'time',
                }
            ),
            'arrival_time': TimeInput( attrs = {
                    'class': 'uk-input',
                    'type': 'time',
                }
            ),
        }
    