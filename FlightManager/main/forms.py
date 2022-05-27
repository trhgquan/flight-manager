from django.forms import ModelForm
from .models import Flight, FlightDetail

class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightDetailForm(ModelForm):
    class Meta:
        model = FlightDetail
        fields = '__all__'