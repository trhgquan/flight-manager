# Typical imports inside views.py
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Messages
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin

# For authentication
from django.contrib.auth import authenticate, login, logout

# Decorators
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from .decorators import unauthenticated_user
from django.views.decorators.http import require_http_methods

# For class-based view
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# For filtered view
from django_filters.views import FilterView
from .filters import *

# For models
from .models import *
from .forms import *

# Services
from .service import *

# Misc
from django.utils.timezone import now

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

            # Decorator redirect
            if request.GET.__contains__('next'):
                return redirect(request.GET.__getitem__('next'))

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

@require_http_methods(['POST'])
@login_required(login_url = 'auth.signin')
def auth_logout(request):
    '''Controller for logging out

    - Requires user to log in.
    '''
    logout(request)
    messages.success(request, 'Successfully logged out, thanks!')
    return redirect('auth.signin')

# Home
class HomepageView(View):
    '''HomepageView, expressed as an OOP class.
    '''
    def __init__(self) -> None:
        self.airport_service = AirportService()

    def get(self, request) -> HttpResponse:
        '''Render homepage, with (of course) airports list.
        '''
        context = {
            'airports' : self.airport_service.findAllAirports(),
        }

        return render(request, 'main/dashboard/dashboard.html', context = context)

class ProfileView(LoginRequiredMixin, View):
    '''ProfileView, expressed as an OOP class.
    '''
    def __init__(self) -> None:
        self.login_url = 'auth.signin'
    
    def get(self, request):
        '''Render Preofile with customer detail.
        '''
        customer = request.user.customer

        context = {
            'customer' : customer,
        }

        return render(request, 'main/profile/view.html', context)

class UpdateProfileView(LoginRequiredMixin, View):
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

        self.login_url = reverse('auth.signin')

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

class UpdatePasswordView(LoginRequiredMixin, View):
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
    redirect_to_success = 'auth.signin'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

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

# Airports

class ListAirportView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    '''ListAirport view, expressed as an OOP class.
    '''

    '''Permissions required to access this view
    '''
    permission_required = 'main.view_airport'

    '''Model used in ListAirportView
    '''
    model = Airport

    '''Maximum rows in a list.
    '''
    paginate_by = 10

    '''HTML template used in ListAirportView
    '''
    template_name = 'main/airport/list.html'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

class CreateAirportView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    '''CreateAirport view, expressed as an OOP class.
    '''

    '''Permissions required to access this view
    '''
    permission_required = 'main.add_airport'

    '''Form used in this View.
    '''
    form_class = AirportForm

    '''HTML template used in this View.
    '''
    template_name = 'main/airport/create.html'

    '''Model used in CreateAirportView
    '''
    model = Airport

    '''Success message
    '''
    success_message = 'Successfully created a new Airport!'
    
    '''Success url (where to redirects after success)
    '''
    success_url = 'airport.update'
    
    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

    def get_success_url(self) -> str:
        return reverse(self.success_url, kwargs = {
            'pk' : self.object.id
        })

class UpdateAirportView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    '''UpdateAirportView, expressed as an OOP class.
    '''

    '''Permissions required to access this view
    '''
    permission_required = 'main.change_airport'

    '''Model used in UpdateAirportView
    '''
    model = Airport

    '''Form used in UpdateAirportView
    '''
    form_class = AirportForm

    '''HTML template used in UpdateAirport.
    '''
    template_name = 'main/airport/update.html'

    '''Success message
    '''
    success_message = 'Successfully updated Airport!'

    '''Success url (where to redirects after success)
    '''
    success_url = 'airport.update'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

    def get_success_url(self) -> str:
        return reverse(self.success_url, kwargs = {
            'pk' : self.object.id
        })

class DeleteAirportView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    '''DeleteAirportView, expressed as an OOP class
    '''

    '''Permissions required to access this view
    '''
    permission_required = 'main.delete_airport'

    '''Model used in DeleteAirportView
    '''
    model = Airport

    '''HTML template used in DeleteAirportView
    '''
    template_name = 'main/airport/delete.html'

    '''Success message
    '''
    success_message = 'Airport removed.'

    '''Where to redirects to after success
    '''
    success_url = 'airport.list'
    
    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

    def get_success_url(self) -> str:
        return reverse(self.success_url)

# Flights

class ListFlightView(ListView):
    '''ListFlightView, expressed as an OOP class.
    '''

    '''Model used in ListFlightView
    '''
    model = Flight

    '''HTML template used in ListFlightView
    '''
    template_name = 'main/flight/list.html'

    '''Maximum flights displaying on list.
    '''
    paginate_by = 10

    def get_queryset(self):
        '''Only show flights from now to the future!
        '''
        return Flight.objects.filter(date_time__gt = now())

class DetailFlightView(DetailView):
    '''DetailFlightView, expressed as an OOP class
    '''

    '''Model used in DetailFlightView
    '''
    model = Flight

    '''HTML template used in DetailFlightView
    '''
    template_name = 'main/flight/detail/view.html'

class CreateFlightView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    '''CreateFlightView, expressed as an OOP class.
    '''

    '''Model used in CreateFlightView
    '''
    model = Flight

    '''Form used in CreateFlightView
    '''
    form_class = FlightForm

    '''Permission required to access this view
    '''
    permission_required = 'main.create_flight'

    '''HTML template used in CreateFlightView
    '''
    template_name = 'main/flight/create.html'

    '''Where to redirects to after success.
    '''
    success_url = 'flight.detail'

    '''Success message to be displayed
    '''
    success_message = 'Flight created successfully!'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')
    
    def get_success_url(self) -> str:
        return reverse(self.success_url, kwargs = {
            'pk' : self.object.id
        })

class UpdateFlightView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    '''UpdateFlightView, expressed as an OOP class
    '''

    '''Model used in UpdateFlightView
    '''
    model = Flight

    '''Form used in UpdateFlightView
    '''
    form_class = FlightForm

    '''HTML template used in UpdateFlightView
    '''
    template_name = 'main/flight/update.html'

    '''Permission(s) required to access this view.
    '''
    permission_required = 'main.change_flight'

    '''Where to redirects to after success.
    '''
    success_url = 'flight.update'

    '''Success message to be displayed
    '''
    success_message = 'Flight updated successfully!'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

    def get_success_url(self) -> str:
        return reverse(self.success_url, kwargs = {
            'pk' : self.object.id
        })

class DeleteFlightView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    '''DeleteFlightView, expressed as an OOP class.
    '''

    '''Model used in DeleteFlightView
    '''
    model = Flight

    '''Permission required to access this view.
    '''
    permission_required = 'main.delete_flight'

    '''HTML template used in DeleteFlightView
    '''
    template_name = 'main/flight/delete.html'

    '''Where to redirects to after success
    '''
    success_url = 'flight.list'

    '''Success message to be displayed
    '''
    success_message = 'Flight deleted successfully.'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

    def get_success_url(self) -> str:
        return reverse(self.success_url)

class UpdateFlightDetailView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    '''UpdateFlightDetailView, expressed as an OOP class
    '''

    '''Model used in UpdateFlightDetailView
    '''
    model = FlightDetail

    '''Form used in UpdateFlightDetailView
    '''
    form_class = FlightDetailForm

    '''Permission required to access this view.
    '''
    permission_required = 'main.change_flight'

    '''HTML template used in UpdateFlightDetailView
    '''
    template_name = 'main/flight/detail/update.html'

    '''Where to redirects to after success.
    '''
    success_url = 'flight.detail.update'

    '''Success message to be displayed.
    '''
    success_message = 'Flight detail updated successfully!'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

    def get_success_url(self) -> str:
        return reverse(self.success_url, kwargs = {
            'pk' : self.object.flight.id
        })
    
    def get_object(self, *args, **kwargs):
        '''This method to load a specific FlightDetail, based on Flight id.
        '''
        flight = Flight.objects.get(id = self.kwargs.get('pk'))
        return FlightDetail.objects.get(flight = flight)

# Transition Airport

class CreateTransitionAirportView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    '''CreateTransitionAirportView, expressed as an OOP class.
    '''

    '''Model used in CreateTransitionAirportView.
    '''
    model = TransitionAirport

    '''Form used in CreateTransitionAirportView.
    '''
    form_class = TransitionAirportForm

    '''HTML template used in CreateTransitionAirportView.
    '''
    template_name = 'main/flight/transition/create.html'

    '''Permissions required to access this view.
    '''
    permission_required = 'main.change_flight'

    '''Where to redirects to after success.
    '''
    success_url = 'flight.detail'

    '''Message to be displayed when success.
    '''
    success_message = 'New transition airport added!'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        
        flight = Flight.objects.get(id = self.kwargs.get('pk'))

        kwargs['route_airports'] = [flight.departure_airport, flight.arrival_airport]
        for transition_airport in flight.transitionairport_set.all():
            kwargs['route_airports'].append(transition_airport.airport)

        return kwargs

    def get_context_data(self, **kwargs):
        '''Since current view does not have parent flight's instance,
        this method will get parent flight's instance and parse it to the view.
        '''
        context = super().get_context_data(**kwargs)

        context['flight'] = Flight.objects.get(id = self.kwargs.get('pk'))

        return context

    def form_valid(self, form) -> HttpResponse:
        '''Automatically set Flight to the Flight requested (aka Flight ID in the URL).
        '''
        form.instance.flight = Flight.objects.get(id = self.kwargs.get('pk'))
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse(self.success_url, kwargs = {
            'pk' : self.kwargs.get('pk')
        })

class UpdateTransitionAirportView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    '''UpdateTransitionAirportView, expressed as an OOP class.
    '''

    '''Model used in UpdateTransitionAirportView
    '''
    model = TransitionAirport

    '''Form used in UpdateTransitionAirportView
    '''
    form_class = TransitionAirportForm

    '''HTML template used in UpdateTransitionAirportView
    '''
    template_name = 'main/flight/transition/update.html'

    '''Permission required to access this view.
    '''
    permission_required = 'main.change_flight'

    '''Where to redirects to after success.
    '''
    success_url = 'flight.transition.update'

    '''Message to be displayed when success.
    '''
    success_message = 'Transition Airport updated successfully!'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        
        flight = self.get_object().flight

        kwargs['route_airports'] = [flight.departure_airport, flight.arrival_airport]
        for transition_airport in flight.transitionairport_set.all():
            kwargs['route_airports'].append(transition_airport.airport)

        return kwargs

    def get_success_url(self) -> str:
        return reverse(self.success_url, kwargs = {
            'pk' : self.object.id
        })

class DeleteTransitionAirportView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    '''DeleteTransitionAirportView, expressed as an OOP class.
    '''

    '''Model used in DeleteTransitionAirportView.
    '''
    model = TransitionAirport

    '''HTML template used in DeleteTransitionAirportView.
    '''
    template_name = 'main/flight/transition/delete.html'

    '''Permissions required to access this view.
    '''
    permission_required = 'main.delete_flight'

    '''Message to be displayed when success.
    '''
    success_message = 'Transition Airport deleted!'

    '''Where to redirects to when success.
    '''
    success_url = 'flight.detail'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')
    
    def get_success_url(self) -> str:
        return reverse(self.success_url, kwargs = {
            'pk' : self.object.flight.id
        })

# Search (Filter)
class FlightSearchView(FilterView):
    '''FlightSearchView, expressed as an OOP class.
    '''

    '''Model used in FlightSearchView
    '''
    model = Flight

    '''Filterset used in FlightSearchView
    '''
    filterset_class = FlightFilter

    '''HTML template used in FlightSearchView
    '''
    template_name = 'main/flight/search.html'

# Booking

class ListFlightTicketView(LoginRequiredMixin, ListView):
    '''ListFlightTicketView, expressed as an OOP class.
    '''

    '''Model used in ListFlightTicketView
    '''
    model = Ticket

    '''HTML template used in ListFlightTicketView
    '''
    template_name = 'main/flight/booking/list.html'

    '''Maximum records in a page.
    '''
    paginate_by = 10

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

    def get_queryset(self):
        '''Users should only see reservations made by them.
        '''
        return Ticket.objects.filter(customer = self.request.user.customer)

class DetailFlightTicketView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    '''DetailFlightTicketView, expressed as an OOP class.
    '''

    '''Model used in DetailFlightTicketView
    '''
    model = Ticket

    '''HTMP template used in DetailFlightTicketView
    '''
    template_name = 'main/flight/booking/detail.html'

    def test_func(self) -> bool:
        '''User can only view his own tickets, except managers.
        '''
        current_customer = self.request.user.customer
        ticket_customer = self.get_object().customer

        if current_customer == ticket_customer:
            return True
        if current_customer.is_in_group('Manager'):
            return True
        return False

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

class CreateFlightTicketView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
    '''CreateFlightTicketView, expressed as an OOP class.
    '''

    '''Model used in CreateFlightTicketView
    '''
    model = Ticket

    '''HTML template used in CreateFlightTicketView
    '''
    template_name = 'main/flight/booking/create.html'

    '''Form used in CreateFlightTicketView
    '''
    form_class = FlightTicketForm

    '''Where to redirects to after success
    '''
    success_url = 'flight.reservation.detail'

    '''Message to be displayed after success.
    '''
    success_message = 'Successfully booked this flight!'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')
    
    def get_success_url(self) -> str:
        return reverse(self.success_url, kwargs = {
            'pk' : self.object.id,
        })

    def get_context_data(self, **kwargs):
        '''Adding additional data to context
        '''
        context = super().get_context_data(**kwargs)

        context["flight"] = Flight.objects.get(id = self.kwargs.get('pk'))

        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['flight'] = Flight.objects.get(id = self.kwargs.get('pk'))
        return kwargs

    def test_func(self) -> bool:
        flight = Flight.objects.get(id = self.kwargs.get('pk'))
        return flight.is_bookable

    def form_valid(self, form) -> HttpResponse:
        '''Automatically add flight, customer and ticket price to form.
        '''
        form.instance.flight = Flight.objects.get(id = self.kwargs.get('pk'))
        form.instance.customer = self.request.user.customer

        # Hardcore ticket adding.
        if form.instance.ticket_class.name == 'First':
            form.instance.price = form.instance.flight.flightdetail.first_class_ticket_price
        elif form.instance.ticket_class.name == 'Economy':
            form.instance.price = form.instance.flight.flightdetail.second_class_ticket_price

        return super().form_valid(form)

class UpdateFlightTicketView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    '''UpdateFlightTicketView, expressed as an OOP class.
    '''

    '''Model used in UpdateFlightTicketView
    '''
    model = Ticket

    '''HTML template used in UpdateFlightTicketView
    '''
    template_name = 'main/flight/booking/update.html'

    '''Form used in UpdateFlightTicketView
    '''
    form_class = FlightTicketForm

    '''Where to redirects to after success
    '''
    success_url = 'flight.reservation.update'

    '''Message to be displayed after success.
    '''
    success_message = 'Reservation updated successfully.'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')
    
    def get_success_url(self) -> str:
        return reverse(self.success_url, kwargs = {
            'pk' : self.object.id,
        })
    
    def test_func(self) -> bool:
        '''User can only update his own unpaid tickets, except managers.
        '''
        if not self.get_object().flight.is_bookable:
            return False

        current_customer = self.request.user.customer
        ticket_customer = self.get_object().customer

        if current_customer == ticket_customer:
            return True
        if current_customer.is_in_group('Manager'):
            return True

        return False

    def form_valid(self, form) -> HttpResponse:
        '''Automatically add flight, customer and ticket price to form.
        '''
        # Hardcore ticket adding.
        if form.instance.ticket_class.name == 'First':
            form.instance.price = form.instance.flight.flightdetail.first_class_ticket_price
        elif form.instance.ticket_class.name == 'Economy':
            form.instance.price = form.instance.flight.flightdetail.second_class_ticket_price

        return super().form_valid(form)

class DeleteFlightTicketView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    '''DeleteFlightTicketView, expressed as an OOP class.
    '''

    '''Model used in DeleteFlightTicketView
    '''
    model = Ticket

    '''HTML template used in DeleteFlightTicketView.
    '''
    template_name = 'main/flight/booking/delete.html'

    '''Where to redirects to after success.
    '''
    success_url = 'flight.reservation.list'

    '''Message to be displayed when success.
    '''
    success_message = 'Cancel reservation successfully.'

    def __init__(self) -> None:
        self.login_url = reverse('auth.signin')

    def get_success_url(self) -> str:
        return reverse(self.success_url)

    def test_func(self) -> bool:
        '''User can only delete his own unpaid tickets, except managers.
        '''
        if not self.get_object().flight.is_bookable:
            return False

        current_customer = self.request.user.customer
        ticket_customer = self.get_object().customer

        if current_customer == ticket_customer:
            return True
        if current_customer.is_in_group('Manager'):
            return True

        return False

def report(request):
    # More HTTP POST processing here

    return render(request, 'main/report.html')