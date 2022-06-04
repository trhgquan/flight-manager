from django import forms
from django.utils.timezone import now
from django_filters import DateFromToRangeFilter, ModelChoiceFilter
from django_filters import FilterSet, widgets

# Models
from .models import *

# Forms
from .forms import *

class FlightFilter(FilterSet):
    departure_airport = ModelChoiceFilter(
        queryset = Airport.objects,
        widget = forms.Select(
            attrs = {
                'class' : 'form-control',
            }
        )
    )
    arrival_airport = ModelChoiceFilter(
        queryset = Airport.objects,
        widget = forms.Select(
            attrs = {
                'class' : 'form-control',
            }
        )
    )
    date_time = DateFromToRangeFilter(
        widget = widgets.RangeWidget(
            attrs = {
                'class' : 'form-control',
                'type' : 'date',
            }
        ),
        label = 'Depart in range',
    )

    class Meta:
        model = Flight
        fields = [
            'departure_airport',
            'arrival_airport',
            'date_time'
        ]