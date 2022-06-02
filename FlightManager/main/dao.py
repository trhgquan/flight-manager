from .models import *
from django.db.models.query import QuerySet

class TicketClassDAO:
    def __init__(self):
        #do nothing
        pass

    #Save a ticket class 
    def create(self, ticketClass: TicketClass) -> TicketClass:
        ticketClass.save()
        return ticketClass
    
    #Assume that before calling update(ticketClass), we already found the ticket class to update
    #   its informations
    def update(self, ticketClass: TicketClass) -> TicketClass:
        ticketClass.save()
        return ticketClass

    #Delete a ticket class with the given id
    def delete(self, id: int) -> int:
        ticketClass = TicketClass.objects.get(pk = id)
        ticketClass.delete()
        return 0
    
    #Find a ticket class with the given id
    def find(self, id: int) -> TicketClass:
        ticketClass = TicketClass.objects.get(pk = id)
        return ticketClass

    #Find all the customers in the database
    def findAll(self) -> QuerySet:
        ticketClasses = TicketClass.objects.all()
        return ticketClasses

class CustomerDAO:
    def __init__(self):
        #do nothing
        pass

    #Save a customer 
    def create(self, customer: Customer) -> Customer:
        customer.save()
        return customer
    
    #Assume that before calling update(customer), we already found the customer to update
    #   its informations
    def update(self, customer: Customer) -> Customer:
        customer.save()
        return customer

    #Delete a customer with the given id
    def delete(self, id: int) -> int:
        customer = Customer.objects.get(pk = id)
        customer.delete()
        return 0
    
    #Find a customer with the given id
    def find(self, id: int) -> Customer:
        customer = Customer.objects.get(pk = id)
        return customer

    #Find all the customers in the database
    def findAll(self) -> QuerySet:

        customers = Customer.objects.all()
        return customers

class AirportDAO:
    def __init__(self):
        #do nothing
        pass

    #Save a airport
    def create(self, airport: Airport) -> Airport:
        airport.save()
        return airport
    
    #Assume that before calling update(airport), we already found the airport to update
    #   its informations
    def update(self, airport: Airport) -> Airport:
        airport.save()
        return airport

    #Delete a airport with the given id
    def delete(self, id: int) -> int:
        airport = Airport.objects.get(pk = id)
        airport.delete()
        return 0
    
    #Find a airport with the given id
    def find(self, id: int) -> Airport:
        airport = Airport.objects.get(pk = id)
        return airport

    #Find all the airports in the database
    def findAll(self) -> QuerySet:
        airports = Airport.objects.all()
        return airports

class TransitionAirportDAO:
    def __init__(self):
        #do nothing
        pass

    #Save a transition airport
    def create(self, transitionAirport: TransitionAirport) -> TransitionAirport:
        transitionAirport.save()
        return transitionAirport
    
    #Assume that before calling update(transitionAirport), we already found the transition airport to update
    #   its informations
    def update(self, transitionAirport: TransitionAirport) -> TransitionAirport:
        transitionAirport.save()
        return transitionAirport

    #Delete a transition airport with the given id
    def delete(self, id: int) -> int:
        transitionAirport = TransitionAirport.objects.get(pk = id)
        transitionAirport.delete()
        return 0
    
    #Find a transition airport with the given id
    def find(self, id: int) -> TransitionAirport:
        transitionAirport = TransitionAirport.objects.get(pk = id)
        return transitionAirport

    #Find all the transition airports in the database
    def findAll(self) -> QuerySet:
        transitionAirports = TransitionAirport.objects.all()
        return transitionAirports

class TicketDAO:
    def __init__(self):
        #do nothing
        pass

    #Save a ticket
    def create(self, ticket: Ticket) -> Ticket:
        ticket.save()
        return ticket
    
    #Assume that before calling update(ticket), we already found the ticket to update
    #   its informations
    def update(self, ticket: Ticket) -> Ticket:
        ticket.save()
        return ticket

    #Delete a ticket with the given id
    def delete(self, id: int) -> int:
        ticket = Ticket.objects.get(pk = id)
        ticket.delete()
        return 0
    
    #Find a ticket with the given id
    def find(self, id: int) -> Ticket:
        ticket = Ticket.objects.get(pk = id)
        return ticket

    #Find all the tickets in the database
    def findAll(self) -> QuerySet:
        tickets = Ticket.objects.all()
        return tickets

class ReservationDAO:
    def __init__(self):
        #do nothing
        pass

    #Save a reservation
    def create(self, reservation: Reservation) -> Reservation:
        reservation.save()
        return reservation
    
    #Assume that before calling update(reservation), we already found the reservation to update
    #   its informations
    def update(self, reservation: Reservation) -> Reservation:
        reservation.save()
        return reservation

    #Delete a reservation with the given id
    def delete(self, id: int) -> int:
        reservation = Reservation.objects.get(pk = id)
        reservation.delete()
        return 0
    
    #Find a reservation with the given id
    def find(self, id: int) -> Reservation:
        reservation = Reservation.objects.get(pk = id)
        return reservation

    #Find all the reservations in the database
    def findAll(self) -> QuerySet:
        reservations = Reservation.objects.all()
        return reservations

class FlightDAO:
    def __init__(self):
        #do nothing
        pass

    #Save a flight
    def create(self, flight: Flight) -> Flight:
        flight.save()
        return flight
    
    #Assume that before calling update(flight), we already found the flight to update
    #   its informations
    def update(self, flight: Flight) -> Flight:
        flight.save()
        return flight

    #Delete a flight with the given id
    def delete(self, id: int) -> int:
        flight = Flight.objects.get(pk = id)
        flight.delete()
        return 0
    
    #Find a flight with the given id
    def find(self, id: int) -> Flight:
        flight = Flight.objects.get(pk = id)
        return flight

    #Find all the flights in the database
    def findAll(self) -> QuerySet:
        flights = Flight.objects.all()
        return flights

class PolicyDAO:
    def __init__(self):
        pass
    
    def create(self, policy: Policy) -> Policy:
        policy.save()
        return policy

    def get(self, id: int) -> Policy:
        policy = Policy.objects.get(id = id)
        return policy
    
    def update(self, update_policy : Policy) -> Policy:
        policy = Policy.objects.get(id = update_policy.id)
        policy.name = update_policy.name
        policy.datatype = update_policy.datatype
        policy.value = update_policy.value
        policy.is_applied = update_policy.is_applied

        policy.save()
        return policy