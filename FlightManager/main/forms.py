from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your username',
        }
    ))
    password = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your password',
        }
    ))
    class Meta:
        model = User,
        fields = [
            'username',
            'password'
        ]

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

#customer
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'