from .dao import *
from .models import *
from .wrapper import FlightStatisticWrapper
from datetime import date, datetime
from random import random

class TicketClassService:
    def __init__(self):
        self.ticketClassDAO = TicketClassDAO()
    
    def createTicketClass(self, ticketClass: TicketClass) -> TicketClass:
        return self.ticketClassDAO.create(ticketClass)
    
    def updateTicketClass(self, ticketClass: TicketClass) -> TicketClass:
        return self.ticketClassDAO.update(ticketClass)

    def deleteTicketClass(self, id: int) -> int:
        return self.ticketClassDAO.delete(id)
    
    def findTicketClassById(self, id: int) -> int:
        return self.ticketClassDAO.find(id)
    
    def findAllTicketClasses(self) -> list:
        return list(self.ticketClassDAO.findAll())

class AirportService:
    def __init__(self):
        self.airportDAO = AirportDAO()
    
    def createAirport(self, airport: Airport) -> Airport:
        return self.airportDAO.create(airport)
    
    def updateAirport(self, airport: Airport) -> Airport:
        return self.airportDAO.update(airport)

    def deleteAirport(self, id: int) -> int:
        return self.airportDAO.delete(id)
    
    def findAirportById(self, id: int) -> int:
        return self.airportDAO.find(id)
    
    def findAllAirports(self) -> list:
        return list(self.airportDAO.findAll())

class TransitionAirportService:
    def __init__(self):
        self.transitionAirportDAO = TransitionAirportDAO()
    
    def createTransitionAirport(self, transitionAirport: TransitionAirport) -> TransitionAirport:
        return self.transitionAirportDAO.create(transitionAirport)
    
    def updateTransitionAirport(self, transitionAirport: TransitionAirport) -> TransitionAirport:
        return self.transitionAirportDAO.update(transitionAirport)

    def deleteTransitionAirport(self, id: int) -> int:
        return self.transitionAirportDAO.delete(id)
    
    def findTransitionAirportById(self, id: int) -> int:
        return self.transitionAirportDAO.find(id)
    
    def findAllTransitionAirports(self) -> list:
        return list(self.transitionAirportDAO.findAll())

class TicketService:
    def __init__(self):
        self.ticketDAO = TicketDAO()
    
    def createTickets(self, tickets: list) -> list:
        
        #Create each ticket
        for ticket in tickets:
            self.ticketDAO.create(ticket)

        return tickets

    
    def updateTickets(self, tickets: list) -> list:

        #Update  each ticket
        for ticket in tickets:
            self.ticketDAO.update(ticket)

        return tickets

    def deleteTickets(self, ids: list) -> int:

        errorCode = 0

        #Try to delete each ticket with the given id
        for id in ids:

            #Save the error code while deleting each ticket
            ec = self.ticketDAO.delete(id)

            #If there is any error => save it
            if 0 != ec:
                errorCode = ec

        return errorCode
    
    def findTicketById(self, id: int) -> int:
        return self.ticketDAO.find(id)
    
    def findAllTickets(self) -> list:
        return list(self.ticketDAO.findAll())

    #Find all the not-booked ticket with the given ticket class from a flight
    def findAvailableTicketsFromFlight(self, flight: Flight, ticketClass: TicketClass) -> list:
        
        result = list()

        #Get all the ticket from the flight
        tickets = list(flight.ticket_set.all())

        #Get the not booked ticket with the correct class
        for ticket in tickets:
            if not ticket.is_booked and ticket.ticket_class_id == ticketClass.id:
                result.append(ticket)

        return result

class ReservationService:
    def __init__(self):
        self.reservationDAO = ReservationDAO()
        self.ticketService = TicketService()
    
    def createReservations(self, reservations: list) -> list:
        
        #Create each reservation
        for reservation in reservations:
            self.reservationDAO.create(reservation)

        return reservations

    
    def updateReservations(self, reservations: list) -> list:

        #Update  each reservation
        for reservation in reservations:
            self.reservationDAO.update(reservation)

        return reservations

    def deleteReservations(self, ids: list) -> int:

        errorCode = 0

        #Try to delete each reservation with the given id
        for id in ids:

            #Save the error code while deleting each reservation
            ec = self.reservationDAO.delete(id)

            #If there is any error => save it
            if 0 != ec:
                errorCode = ec

        return errorCode
    
    def findReservationById(self, id: int) -> int:
        return self.reservationDAO.find(id)
    
    def findAllReservations(self) -> list:
        return list(self.reservationDAO.findAll())

    #Find all the reservations for the not-booked ticket with the given ticket class from a flight
    def findAvailableReservationsFromFlight(self, flight: Flight, ticketClass: TicketClass) -> list:
        
        reservations = list()

        #Get the available tickets
        tickets = self.ticketService.findAvailableTicketsFromFlight(flight, ticketClass)

        #Get the reservation from the found tickets
        for ticket in tickets:
            reservations.append(ticket.reservation)

        return reservations

class FlightService:
    def __init__(self):
        self.flightDAO = FlightDAO()
    
    def createFlight(self, flight: Flight) -> Flight:
        return self.flightDAO.create(flight)
    
    def updateFlight(self, flight: Flight) -> Flight:
        return self.flightDAO.update(flight)

    def deleteFlight(self, id: int) -> int:
        return self.flightDAO.delete(id)
    
    def findFlightById(self, id: int) -> int:
        return self.flightDAO.find(id)
    
    def findAllFlights(self) -> list:
        return list(self.flightDAO.findAll())

    #Find a list of flights by the given criterias
    def findFlightByCriterias(self, departureAirport: Airport, arrivalAirport: Airport, date_time: datetime, startDate: date, endDate: date) -> list:
        
        result: list()
        flights = self.findAllFlights()

        #Filtering the airports
        for flight in flights:

            #Flag to check if a flight is already add to optimizing
            isAdd = False

            #Filter by departure airport
            if False == isAdd and departureAirport is not None: 
                if flight.departure_airport_id == departureAirport.id:
                    result.append(flight)
                    isAdd = True

            #Filter by arrival airport
            if False == isAdd and arrivalAirport is not None: 
                if flight.arrival_airport_id == arrivalAirport.id:
                    result.append(flight)
                    isAdd = True
            
            #Filter by datetime
            if False == isAdd and date_time is not None: 
                if flight.date_time == date_time:
                    result.append(flight)
                    isAdd = True

            #Filtering by range
            date = flight.date_time.date()  #Get date from datetime of a flight
            if False == isAdd and startDate is not None and endDate is not None:
                if startDate <= date and date <= endDate:
                    result.append(flight)
                    isAdd = True

            else:

                #Filtering by start date
                if False == isAdd and startDate is not None:
                    if startDate <= date:
                        result.append(flight)
                        isAdd = True

                else:

                    #Filtering by end date
                    if False == isAdd and endDate is not None:
                        if date <= endDate:
                            result.append(flight)
                            isAdd = True

            return result

    def findFlightToReport(self, month: int, year: int) -> list:
        
        result = list()
        flights = self.findAllFlights()

        for flight in flights:
        
            #Get the date from each flight
            date = flight.date_time.date()

            #If month is not None => report by month
            if  month is not None:
                if date.year == year and date.month == month:
                    result.append(flight)

            #Else => report by year
            else:
                if date.year == year:
                    result.append(flight)

        return result
    
class ReportService:
    def __init__(self):
        self.flightService = FlightService()

    def getReportByMonth(self, month: int, year: int) -> list:
        wrappers = list()

        flights = self.flightService.findFlightToReport(month, year)
        for flight in flights:
            wrapper = FlightStatisticWrapper(flight)
            wrappers.append(wrapper)
        
        return wrappers
    
    def getReportByYear(self, year: int) -> list:
        wrappers = list()

        flights = self.flightService.findFlightToReport(None, year)
        for flight in flights:
            wrapper = FlightStatisticWrapper(flight)
            wrappers.append(wrapper)
        
        return wrappers

class PolicyService:
    def __init__(self):
        #do nothing
        pass

    def isLateToBook(self) -> bool:
        #TODO:

        return False

    def isLateToCancel(self) -> bool:
        #TODO:

        return False

class CustomerService:
    def __init__(self):
        self.customerDAO = CustomerDAO()
        self.policyService = PolicyService()
        self.reservationService = ReservationService()
        self.ticketService = TicketService()

    def createCustomer(self, customer: Customer) -> Customer:
        return self.customerDAO.create(customer)
    
    def updateCustomer(self, customer: Customer) -> Customer:
        return self.customerDAO.update(customer)

    def deleteCustomer(self, id: int) -> int:
        return self.customerDAO.delete(id)
    
    def findCustomerById(self, id: int) -> int:
        return self.customerDAO.find(id)
    
    def findAllCustomers(self) -> list:
        return list(self.customerDAO.findAll())

    #Book a ticket from a flight with a given ticket class
    def book(self, customer: Customer, flight: Flight, ticketClass: TicketClass, name: str, phone: str, identity_code: str) -> Reservation:

        #Check if the current time is late to book the flight
        if self.policyService.isLateToBook():
            return None

        #Get the all the reservations with the given ticket class in the flight 
        reservations = self.reservationService.findAvailableReservationsFromFlight(flight, ticketClass)

        #Choose the reservation randomizely
        reservation = random.choices(reservations)
        ticket = reservation.ticket

        #Fill the reservation field
        reservation.date_booked = date.today()

        #Fill the ticket field
        ticket.is_booked = True
        ticket.customer = customer
        ticket.name = name
        ticket.phone = phone
        ticket.identity_code = identity_code

        #Make the ticket and reservation become a list, to reuse the code
        tickets = list()
        reservations = list()
        tickets.append(ticket)
        reservations.append(reservation)

        #Update the data in database
        self.ticketService.updateTicket(tickets)
        self.reservationService.updateReservations(reservations)

        return reservation

    #Cancel a flight booking
    def cancel(self, reservation: Reservation) -> int:

        #Check if the current time is late to cancel the flight
        if self.policyService.isLateToCancel():
            return 1
        
        #Get the ticket from the reservation
        ticket = reservation.ticket

        #Fill the reservation field
        reservation.date_booked = None

        #Fill the ticket field
        ticket.is_booked = False
        ticket.customer =  None
        ticket.name = None
        ticket.phone = None
        ticket.identity_code = None

        #Make the ticket and reservation become a list, to reuse the code
        tickets = list()
        reservations = list()
        tickets.append(ticket)
        reservations.append(reservation)

        #Update the data in database
        self.ticketService.updateTicket(tickets)
        self.reservationService.updateReservations(reservations)

        return 0