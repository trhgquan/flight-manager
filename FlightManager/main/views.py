from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/dashboard.html')

def flights(request):
    return render(request, 'accounts/flights.html')

def customers(request):
    return render(request, 'accounts/customers.html')