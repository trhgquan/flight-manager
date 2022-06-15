from django.db.models import Sum, Count, Q
from django.db.models.functions import Coalesce, TruncMonth
from django.shortcuts import get_object_or_404

from .dao import *
from .models import *

class AirportService:
    def __init__(self):
        self.airport_dao = Airport.objects
    
    def get_airport_list_queryset(self):
        '''Get all airports
        '''
        return self.airport_dao.all()

class TicketService:
    def __init__(self):
        self.ticket_dao = Ticket.objects

    def get_ticket(self, ticket_id : int) -> Ticket:
        '''Get ticket with the given ID, or return 404.
        '''
        return get_object_or_404(self.ticket_dao, id = ticket_id)

    def get_ticket_list_queryset(self, customer : Customer) -> QuerySet:
        '''Load ticket list of a customer
        '''
        related_fields = [
            'flight',
            'ticket_class',
        ]

        return self.ticket_dao.filter(
            customer = customer
        ).prefetch_related(*related_fields)

class FlightService:
    def __init__(self) -> None:
        self.flight_dao = Flight.objects
        self.flight_detail_dao = FlightDetail.objects

    def total_flights(self, year : int) -> int:
        '''Get total flights in a year.
        '''
        return self.flight_dao.filter(
            date_time__year = year,
            date_time__lt = now(),
        ).count()

    def total_tickets_sold(self, year : int) -> int:
        '''Get total tickets sold in a year.
        '''
        return sum(self.flight_dao.filter(
            date_time__year = year,
            date_time__lt = now(),
        ).annotate(
            tickets_sold = Count(
                'ticket__id',
                filter = Q(ticket__is_booked = True),
            )
        ).values_list('tickets_sold', flat = True))

    def total_revenue(self, year : int) -> int:
        '''Get total revenue of a year.
        '''
        return sum(self.flight_dao.filter(
            date_time__year = year,
            date_time__lt = now(),
        ).annotate(
            revenue = Coalesce(Sum(
                'ticket__price',
                filter = Q(ticket__is_booked = True),
            ), 0)
        ).values_list('revenue', flat = True))

    def get_flight(self, flight_id : int) -> Flight:
        '''Get flight and return 404 if not found.
        '''
        return get_object_or_404(self.flight_dao, id = flight_id)
    
    def get_flight_detail(self, flight_id : int) -> FlightDetail:
        '''Get flight detail.
        '''
        flight = get_object_or_404(self.flight_dao, id = flight_id)
        return get_object_or_404(self.flight_detail_dao, flight = flight)

    def get_flight_list_queryset(self) -> QuerySet:
        '''Get flight list queryset.
        '''
        related_fields = [
            'flightdetail',
            'departure_airport',
            'arrival_airport',
        ]

        return self.flight_dao.filter(
            date_time__gt = now()
        ).prefetch_related(*related_fields)

    def get_search_queryset(self, queryset : QuerySet) -> QuerySet:
        '''Get search queryset
        '''
        related_fields = [
            'departure_airport',
            'arrival_airport',
            'flightdetail',
        ]

        return queryset.filter(
            date_time__gt = now()
        ).prefetch_related(*related_fields)

    def get_general_report_queryset(self, queryset : QuerySet) -> QuerySet:
        '''Get general report queryset.
        '''
        return queryset.filter(
            date_time__lt = now()
        ).prefetch_related(
            'flightdetail'
        ).annotate(
            revenue = Coalesce(Sum(
                'ticket__price',
                filter = Q(ticket__is_booked = True),
            ), 0)
        ).order_by('date_time')

    def get_yearly_report_queryset(self, queryset : QuerySet, year : int) -> QuerySet:
        '''Get yearly report queryset.
        '''
        return queryset.filter(
            date_time__year = year,
            date_time__lt = now(),
        ).annotate(
            month = TruncMonth('date_time')
        ).values(
            'month'
        ).annotate(
            total_flights = Count('id', distinct = True)
        ).annotate(
            total_tickets_sold = Count(
                'ticket__id',
                filter = Q(ticket__is_booked = True),
            )
        ).annotate(
            revenue = Coalesce(Sum(
                'ticket__price',
                filter = Q(ticket__is_booked = True),
            ), 0)
        ).order_by('month')

class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDAO()

    def create_customer(self, customer: Customer) -> Customer:
        '''Create a new customer
        '''
        return self.customer_dao.create(customer)
    
    def update_customer(self, customer: Customer) -> Customer:
        '''Update customer
        '''
        return self.customer_dao.update(customer)