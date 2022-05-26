from django.shortcuts import render
from django.http import HttpResponse

from .models import Airport

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard/dashboard.html')

def flights(request):
    return render(request, 'accounts/flights.html')

def customer(request):
    return render(request, 'accounts/customer.html')

def airport_list(request):
    list = Airport.objects.all()
    print(list)
    return render(request, 'airport/airport_list.html', {'airports':list})