from django.shortcuts import render
from django.http import HttpResponse

#from FlightManager.main.models import Flight
from .models import *

# Create your views here.

# Authenticate
def signup(request):
    # More processing for POST method here.

    return render(request, 'main/signup.html')

def login(request):
    # More processing for POST method here.

    return render(request, 'main/login.html')

def home(request):
    return render(request, 'main/dashboard/dashboard.html')

def flightList(request):
	flights = Flight.objects.all()
	return render(request, 'main/flight/flightList.html', {'flights' : flights})

def flightDetail(request, pk):
    detail = FlightDetail.objects.get(id=pk)
    context = {'detail' : detail}
    return render(request, 'main/flight/flightDetail.html', context)


def customer(request):
    return render(request, 'main/customer.html')

def report(request):
    # More HTTP POST processing here

    return render(request, 'main/report.html')