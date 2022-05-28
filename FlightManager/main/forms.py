from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

# Authentication forms
class LoginForm(AuthenticationForm):
    '''Login form

    Required fields:
        - username
        - password
    '''
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

class RegisterForm(UserCreationForm):
    '''Register form

    Required fields:
        - username (unique)
        - password1
        - password2 (must match with password1)
        - email (valid email)
    '''
    username = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your username',
        }
    ))
    email = forms.CharField(widget = forms.EmailInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your email',
        },
    ))
    password1 = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Your password',
        },
    ), label = 'Your password')
    password2 = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Confirm your password',
        }
    ), label = 'Confirm your password')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
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
        exclude = [
            'user',
        ]
    
        widgets = {
            'name' : forms.TextInput(attrs = {
                'class' : 'form-control'
            }),
            'phone' : forms.TextInput(attrs = {
                'class' : 'form-control'
            }),
            'identity_code' : forms.TextInput(attrs = {
                'class' : 'form-control'
            }),
        }