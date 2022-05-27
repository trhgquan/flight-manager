from django.forms import ModelForm

from .models import *

class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightDetailForm(ModelForm):
    class Meta:
        model = FlightDetail
        fields = '__all__'

class AirportForm(ModelForm):
    class Meta:
        model = Airport
        fields = '__all__'