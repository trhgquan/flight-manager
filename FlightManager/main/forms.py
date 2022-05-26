from django.forms import ModelForm
from .models import Flight

class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'