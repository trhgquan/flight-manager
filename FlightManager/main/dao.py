from models import *
from django.db.models.query import QuerySet

class TicketClassDAO:

    __init__(self):
        #do nothing

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

    __init__(self):
        #do nothing

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

