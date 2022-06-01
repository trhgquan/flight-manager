from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .models import *
from .service import *

def customer_profile(sender, instance, created, **kwargs):
    '''Create a Customer profile when a new User is created.
    '''
    if created:
        # Add to group later

        # Create a new Customer and link it with the newly-created User.
        new_customer = Customer(user = instance)

        # Using Service (wth?) to create.
        customer_service = CustomerService()
        customer_service.createCustomer(new_customer)

def flight_detail(sender, instance, created, **kwargs):
    '''Create a Detail when a new Flight is created
    '''
    if created:
        new_flight_detail = FlightDetail(flight = instance)

        new_flight_detail.save()

post_save.connect(customer_profile, sender = User)
post_save.connect(flight_detail, sender = Flight)