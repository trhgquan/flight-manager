from dao import *

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