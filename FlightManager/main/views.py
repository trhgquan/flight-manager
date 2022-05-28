# Typical imports inside views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

# For authentication
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user

# For models
from .models import *
from .forms import *

# Services
from .service import *

# Create your views here.

# Authenticate
@unauthenticated_user
def auth_signup(request):
    '''Controller for creating new User.

    - with any methods differ than POST: render register page
    - else: try to create a new User.

    Notice that this will create a new User, with blank customer info.
    Customer will fill out these infos later.
    '''
    # Handling register request
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # Save user to database
            form.save()

            user_instance = form.instance.username

            messages.success(request, f'Successfully created an account {user_instance.username}')
           
            return redirect('auth.signin')
        else:
            error_list = form.errors.as_data
            messages.error(request, error_list)

    form = RegisterForm()

    context = {
        'form' : form
    }

    return render(request, 'main/auth/signup.html', context)

@unauthenticated_user
def auth_signin(request):
    '''Controller for signing in

    - with any methods differ than POST: render login page
    - else: try to log user in.
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect, please try again.')

    form = LoginForm()

    context = {
        'form' : form,
    }

    return render(request, 'main/auth/login.html', context)

@login_required(login_url = 'auth.signin')
def auth_logout(request):
    '''Controller for logging out

    - Requires user to log in.
    '''
    logout(request)
    messages.success(request, 'Successfully logged out, thanks!')
    return redirect('auth.signin')

def home(request):
    '''Home, aka Dashboard
    '''
    return render(request, 'main/dashboard/dashboard.html')

@login_required(login_url = 'auth.signin')
def profile_view(request):
    '''User profile
    '''

    customer = request.user.customer

    context = {
        'customer' : customer,
    }

    return render(request, 'main/profile/view.html', context)

@login_required(login_url = 'auth.signin')
def profile_update_information(request):
    '''Update user profile.
    '''

    customer = request.user.customer

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance = customer)

        if form.is_valid():
            # Calling services to handle model update.
            customer_service = CustomerService()

            customer_service.updateCustomer(form.instance)

            messages.success(request, 'Your changes are saved!')

            return redirect('profile.update_information')
        else:
            error_messages = ''.join(message for message in form.error_messages.keys())

            messages.error(request, f'Something went wrong: {error_messages}')

    form = CustomerForm(instance = customer)

    context = {
        'customer_form' : form,
    }

    return render(request, 'main/profile/update.html', context)

@login_required(login_url = 'auth.signin')
def profile_update_password(request):
    '''Update user's password
    '''
    if request.method == 'POST':
        # ChangePasswordForm requires user instance
        form = ChangePasswordForm(request.user, request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Your password has been changed!')

            return redirect('profile.update_password')
        else:
            errors_list = form.errors.as_data

            messages.error(request, errors_list)

    form = ChangePasswordForm(request.user)

    context = {
        'form' : form,
    }

    return render(request, 'main/auth/change_password.html', context)

def flightList(request):
    flights = Flight.objects.all()
    return render(request, 'main/flight/flightList.html', {'flights' : flights})

def flightDetail(request, pk):
    detail = FlightDetail.objects.get(id=pk)
    context = {'detail' : detail}
    return render(request, 'main/flight/flightDetail.html', context)

def flightCreate(request):
    form = FlightForm()

    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form' : form}

    return render(request, 'main/flight/flightForm.html', context)

def flightDetailCreate(request):
    form = FlightDetailForm()

    if request.method == 'POST':
        form = FlightDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render(request, 'main/flight/flightForm.html', context)

def flightUpdate(request, pk):
    flight = Flight.objects.get(id=pk)
    form = FlightForm(instance=flight)

    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('/flight/list')
    
    context = {'form' : form}
    return render(request, 'main/flight/flightForm.html', context)

def flightDetailUpdate(request, pk):
    detail = FlightDetail.objects.get(id=pk)
    form = FlightDetailForm(instance=detail)

    if request.method == 'POST':
        form = FlightDetailForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('/flight/list')
    
    context = {'form' : form}
    return render(request, 'main/flight/flightForm.html', context)

def flightDelete(request, pk):
    flight = Flight.objects.get(id=pk)
    
    if request.method == 'POST':
        flight.delete()
        return redirect('/flight/list')

    context = {'item' : flight}
    return render(request, 'main/flight/flightDelete.html', context)

def customer(request):
    return render(request, 'customer/customer_list.html')

def booking(request):
    return render(request, 'main/booking.html')

def report(request):
    # More HTTP POST processing here

    return render(request, 'main/report.html')

def airport_list(request):
    list = Airport.objects.all()
    print(list)
    return render(request, 'airport/airport_list.html', {'airports':list, 'nbar': 'airport_list'})

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

#customer
def customerPer(request):
    return render(request, 'customer/customer_per.html')

def createCustomer(request):
    form= CustomerForm()
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'customer/customer_form.html', context)

def updateCustomer(request):
    return render(request,'customer/customer_update.html')

def deleteCustomer(request):
    return render(request,'customer/customer_delete.html')