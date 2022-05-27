from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Airport)
admin.site.register(TransitionAirport)
admin.site.register(Flight)
admin.site.register(FlightDetail)
admin.site.register(TicketClass)
admin.site.register(Ticket)
admin.site.register(Reservation)
admin.site.register(Policy)