from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Account infc
class Customer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    identity_code = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(default = "logo.png", null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Manager(Customer):

    def __str__(self):
        return self.name

class Admin(Manager):

    def __str__(self):
        return self.name

class Airport(models.Model):

    name = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
class TransitionAirport(models.Model):

    airport = models.ForeignKey(Airport, null = True, on_delete = models.SET_NULL)
    transition_time =  models.IntegerField(null = True) #minutes
    note = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True)

class Flight(models.Model):
    departure_airport = models.ForeignKey(Airport, null = True, on_delete = models.SET_NULL, related_name = "departure_airport")
    arrival_airport = models.ForeignKey(Airport, null = True, on_delete = models.SET_NULL, related_name = "arrival_airport")
    date_time = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add = True)
    transition_aiports = models.ManyToManyField(TransitionAirport)

class FlightDetail(models.Model):

    flight = models.OneToOneField(Flight, null = True, blank = True, on_delete = models.CASCADE)
    flight_time =  models.IntegerField(null = True)             #minutes
    first_class_seat_size = models.IntegerField(null = True)
    second_class_seat_size = models.IntegerField(null = True)
    date_created = models.DateTimeField(auto_now_add = True)

class TicketClass(models.Model):

    name = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Ticket(models.Model):

    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    flight = models.ForeignKey(Flight, null = True, on_delete = models.SET_NULL)
    ticket_class = models.ForeignKey(TicketClass, null = True, on_delete = models.SET_NULL)

    #name of the person own the ticket
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    identity_code = models.CharField(max_length = 200, null = True)

    is_booked = models.BooleanField(null = True, default = False)
    price = models.IntegerField(null = True)
    date_created = models.DateTimeField(auto_now_add = True)

class Reservation(models.Model):
    ticket = models.OneToOneField(Ticket, null = True, blank = True, on_delete = models.CASCADE)
    date_booked = models.DateField()
    date_created = models.DateTimeField(auto_now_add = True)

class Policy(models.Model):

    name = models.CharField(max_length = 200, null = True)
    datatype = models.CharField(max_length = 200, null = True)
    value = models.IntegerField(null = True)
    is_applied = models.BooleanField(null = True, default = False)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

