# Typical imports inside views.py
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseGone

# For authentication
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from .decorators import unauthenticated_user

# For models
from .models import *
from .forms import *

# Services
from .service import *

# Create your views here.

# Authentication views
class LoginView(View):
    '''Login View, expressed as an OOP class.
    '''

    '''HTML template for Login view.
    '''
    template_name = 'main/auth/login.html'

    '''Form used for LoginView
    '''
    form_class = LoginForm

    '''Where to redirect after a successful login.
    '''
    redirect_to_success = 'home'

    '''Where to redirect if something went wrong.
    '''
    redirect_to_fails = 'auth.signin'

    @method_decorator(unauthenticated_user)
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        '''Applies decorator to all methods inside this class
        '''
        return super().dispatch(request, *args, **kwargs)

    def get(self, request : HttpRequest, *args, **kwargs) -> HttpResponse:
        '''Login screen, aka what the user see when accessing Login page.
        '''
        form = self.form_class

        context = {
            'form' : form
        }

        return render(request, self.template_name, context)
    
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        '''Login processing (with POST)
        '''
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)

            return redirect(self.redirect_to_success)
    
        messages.error(request, 'Username or Password is incorrect, please try again.')

        return redirect(self.redirect_to_fails)

class RegisterView(View):
    '''Register View, expressed as an OOP class.
    '''

    '''HTML template for Sign up view
    '''
    template_name = 'main/auth/signup.html'

    '''Form used for RegisterForm
    '''
    form_class = RegisterForm

    '''Where to redirect to after a new account was created.
    '''
    redirect_to_success = 'auth.signin'

    @method_decorator(unauthenticated_user)
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        '''Register screen aka what the user see when accessing Register route.
        '''
        form = self.form_class

        context = {
            'form' : form
        }

        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        '''Register processing (POST)
        '''
        form = self.form_class(request.POST)

        if form.is_valid():
            # Save form data to a new User instance.
            form.save()

            username = form.cleaned_data.get('username')

            messages.success(request, f'Successfully created {username}, now you can sign in!')

            return redirect(self.redirect_to_success)
        
        # Form is not valid, return error message to the user.

        context = {
            'form' : form,
        }

        return render(request, self.template_name, context)

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

# Profile views
@login_required(login_url = 'auth.signin')
def profile_view(request):
    '''User profile
    '''

    customer = request.user.customer

    context = {
        'customer' : customer,
    }

    return render(request, 'main/profile/view.html', context)

class UpdateProfileView(View):
    '''UpdateProfileView, expressed as an OOP class.
    '''

    '''HTML template for UpdateProfileView
    '''
    template_name = 'main/profile/update.html'

    '''Form used for CustomerForm
    '''
    form_class = CustomerForm

    '''Where to redirect to after profile updated successfully
    '''
    redirect_to_success = 'profile.update_information'

    '''Where to redirect to when something went wrong.
    '''
    redirect_to_fails = 'profile.update_information'

    def __init__(self) -> None:
        '''Initialise - services goes here
        '''
        self.customer_service = CustomerService()

    @method_decorator(login_required(login_url = 'auth.signin'))
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        '''Update Profile screen, aka what the user see when accessing Update Profile page.
        '''
        form = self.form_class(instance = request.user.customer)

        context = {
            'form' : form,
        }

        return render(request, self.template_name, context)
    
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        '''UpdateProfile processing (POST)
        '''
        form = self.form_class(request.POST, request.FILES, instance = request.user.customer)

        if form.is_valid():
            self.customer_service.updateCustomer(form.instance)

            messages.success(request, 'Your changes are saved!')

            return redirect(self.redirect_to_success)

        # Return form with errors.
        context = {
            'form' : form,
        }

        return render(request, self.template_name, context)

class UpdatePasswordView(View):
    '''UpdatePasswordView, expressed as an OOP class.
    '''

    '''Form used in ChangePasswordView.
    '''
    form_class = ChangePasswordForm

    '''HTML template for Change Password view.
    '''
    template_name = 'main/auth/change_password.html'

    '''Where to redirects to after something went wrong.
    '''
    redirect_to_success = 'home'

    @method_decorator(login_required(login_url = 'auth.signin'))
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        '''UpdatePassword screen aka what the user see when accessing UpdatePassword route.
        '''
        form = self.form_class(request.user)

        context = {
            'form' : form,
        }

        return render(request, self.template_name, context)
    
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        '''UpdatePassword processing (POST)
        '''
        form = self.form_class(request.user, request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Your password has been changed!')
        
            # User will be automatically logged-out here,
            return redirect(self.redirect_to_success)
        
        context = {
            'form' : form,
        }

        return render(request, self.template_name, context)

class CreateAirportView(View):
    form_class = AirportForm

    template_name = 'main/airport/form.html'

    redirect_to_success = 'airport.list'

    def __init__(self):
        self.airport_service = AirportService()

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.form_class()

        context = {
            'form' : form
        }

        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.form_class(request.POST)

        if form.is_valid():
            airport = self.airport_service.createAirport(form.instance)

            messages.success(request, f'Added new airport {airport.name} successfully!')

            return redirect(self.redirect_to_success)

        context = {
            'form' : form,
        }

        return render(request, self.template_name, context)

class UpdateAirportView(CreateAirportView):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.form_class()

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
    return render(request, 'main/airport/list.html', {'airports':list, 'nbar': 'airport_list'})

def createAirport(request):
    form = AirportForm()
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/airport/list')

    context = {'form': form}
    return render(request, 'main/airport/add.html', context)

def updateAirport(request, pk):

    airport = Airport.objects.get(id=pk)
    form = AirportForm(instance=airport)

    if request.method == 'POST':
        form = AirportForm(request.POST, instance=airport)
        if form.is_valid():
            form.save()
            return redirect('/airport/list')

    context = {'form':form}
    return render(request, 'main/airport/create.html', context)

def deleteAirport(request, pk):
    airport = Airport.objects.get(id=pk)
    if request.method == "POST":
        airport.delete()
        return redirect('/airport/list')

    context = {'item':airport}
    return render(request, 'main/airport/delete.html', context)

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