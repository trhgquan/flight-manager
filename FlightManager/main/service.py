from dao import *
from models import *

class TicketClassService:
    
    ticketClassDAO: TicketClassDAO

    def __init__(self):
        ticketClassDAO = TicketClassDAO()
    
    def createTicketClass(self, ticketClass: TicketClass) -> TicketClass:
        return ticketClassDAO.create(ticketClass)
    
    def updateTicketClass(self, ticketClass: TicketClass) -> TicketClass:
        return ticketClassDAO.update(ticketClass)

    def deleteTicketClass(self, id: int) -> int:
        return ticketClassDAO.delete(id)
    
    def findTicketClassById(self, id: int) -> int:
        return ticketClassDAO.find(id)
    
    def findAllTicketClasses(self) -> list:
        return list(ticketClassDAO.findAll())

class AirportService:
    
    airportDAO: AirportDAO

    def __init__(self):
        airportDAO = AirportDAO()
    
    def createAirport(self, airport: Airport) -> Airport:
        return airportDAO.create(airport)
    
    def updateAirport(self, airport: Airport) -> Airport:
        return airportDAO.update(airport)

    def deleteAirport(self, id: int) -> int:
        return airportDAO.delete(id)
    
    def findAiportById(self, id: int) -> int:
        return airportDAO.find(id)
    
    def findAllAirports(self) -> list:
        return list(airportDAO.findAll())

class TransitionAirportService:
    
    transitionAirportDAO: TransitionAirportDAO

    def __init__(self):
        transitionAirportDAO = TransitionAirportDAO()
    
    def createTransitionAirport(self, transitionAirport: TransitionAirport) -> TransitionAirport:
        return transitionAirportDAO.create(transitionAirport)
    
    def updateTransitionAirport(self, transitionAirport: TransitionAirport) -> TransitionAirport:
        return transitionAirportDAO.update(transitionAirport)

    def deleteTransitionAirport(self, id: int) -> int:
        return transitionAirportDAO.delete(id)
    
    def findTransitionAirportById(self, id: int) -> int:
        return transitionAirportDAO.find(id)
    
    def findAllTransitionAirports(self) -> list:
        return list(transitionAirportDAO.findAll())

class TicketService:
    
    ticketDAO: TicketDAO

    def __init__(self):
        ticketDAO = TicketDAO()
    
    def createTickets(self, tickets: list) -> list:
        
        #Create each ticket
        for ticket in tickets:
            ticketDAO.create(ticket)

        return tickets

    
    def updateTicket(self, tickets: list) -> list:

        #Update  each ticket
        for ticket in tickets:
            ticketDAO.update(ticket)

        return tickets

    def deleteTicket(self, ids: list) -> int:

        errorCode = 0

        #Try to delete each ticket with the given id
        for id in ids:

            #Save the error code while deleting each ticket
            ec = ticketDAO.delete(id)

            #If there is any error => save it
            if 0 != ec:
                errorCode = ec

        return errorCode
    
    def findTicketById(self, id: int) -> int:
        return ticketDAO.find(id)
    
    def findAllTickets(self) -> list:
        return list(ticketDAO.findAll())

class ReservationService:
    
    reservationDAO: ReservationDAO

    def __init__(self):
        reservationDAO = ReservationDAO()
    
    def createReservations(self, reservations: list) -> list:
        
        #Create each reservation
        for reservation in reservations:
            reservationDAO.create(reservation)

        return reservations

    
    def updateReservation(self, reservations: list) -> list:

        #Update  each reservation
        for reservation in reservations:
            reservationDAO.update(reservation)

        return reservations

    def deleteReservation(self, ids: list) -> int:

        errorCode = 0

        #Try to delete each reservation with the given id
        for id in ids:

            #Save the error code while deleting each reservation
            ec = reservationDAO.delete(id)

            #If there is any error => save it
            if 0 != ec:
                errorCode = ec

        return errorCode
    
    def findReservationById(self, id: int) -> int:
        return reservationDAO.find(id)
    
    def findAllReservations(self) -> list:
        return list(reservationDAO.findAll())