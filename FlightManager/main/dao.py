from models import *

class CustomerDAO():

    __init__(self):
        #do nothing

    def create(self, customer: Customer) -> Customer:
        customer.save()
        return customer
    
    #Assume that before calling update(customer), we already found the customer to update
    #   its informations
    def update(self, customer: Customer) -> Customer:
        original = customer.save()
        return customer

    def delete(self, id: int) -> int:
        customer = Customer.objects.get(pk = id)
        customer.delete()
        return 0
    
    def find(self, id: int) -> Customer:
        customer = Customer.objects.get(pk = id)
        return customer

    def findAll(self) -> QuerySet:

        customers = Customer.objects.all()
        return customers

