from socket import AI_PASSIVE
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import AirportForm

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

def createAirport(request):
    form = AirportForm()
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/airport/list')

    context = {'form': form}
    return render(request, 'airport/airport_form.html', context)

def updateAirport(request, pk):

	airport = Airport.objects.get(id=pk)
	form = AirportForm(instance=airport)

	if request.method == 'POST':
		form = AirportForm(request.POST, instance=airport)
		if form.is_valid():
			form.save()
			return redirect('/airport/list')

	context = {'form':form}
	return render(request, 'airport/airport_form.html', context)

def deleteAirport(request, pk):
	airport = Airport.objects.get(id=pk)
	if request.method == "POST":
		airport.delete()
		return redirect('/airport/list')

	context = {'item':airport}
	return render(request, 'airport/delete.html', context)