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
    
