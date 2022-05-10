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

class TicketClass(models.Model):

    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name

class Ticket(models.Model):

    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    flight = models.ForeignKey(Flight, null = True, on_delete = models.SET_NULL)
    ticket_class = models.ForeignKey(TicketClass, null = True, on_delete = models.SET_NULL)
    price = models.IntegerField(null = True)
    date_created = models.DateTimeField(auto_now_add = True)

class Reservation(models.Model):

    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    flight = models.ForeignKey(Flight, null = True, on_delete = models.SET_NULL)
    ticket_class = models.ForeignKey(TicketClass, null = True, on_delete = models.SET_NULL)
    price = models.IntegerField(null = True)
    date_booked = models.DateField()
    date_created = models.DateTimeField(auto_now_add = True)

class Airport(models.Model):

    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name
    
class TransitionAirport(models.Model):

    airport = models.ForeignKey(Airport, null = True, on_delete = models.SET_NULL)
    transition_time =  models.IntegerField(null = True) #minutes
    note = models.CharField(max_length = 200, null = True)