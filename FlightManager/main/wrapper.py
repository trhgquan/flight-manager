from models import Flight

class FlightStatisticWrapper:
    __flight: Flight
    __numberOfEmptySeat: int
    __numberOfSeat: int
    __turnover: int

    def __init__(self, flight: Flight):
        self.__flight = flight
        self.update()

    #Update data after retrieving the flight
    def update(self) -> None:

        #Reset the counter
        self.__numberOfEmptySeat = 0
        self.__numberOfSeat = 0
        

        #Count the number of ticket which isn't booked
        tickets = self.__flight.ticket_set.all()
        for ticket in tickets:
            self.__numberOfSeat += 1
            if not ticket.is_booked:
                self.__numberOfEmptySeat  += 1
            else:
                self.__turnover += ticket.price

    def numberOfEmptySeat(self) -> int:
        return self.__numberOfEmptySeat
    
    def numberOfAllSeat(self) -> int:
        return self.__numberOfSeat
    
    def numberOfBookedSeat(self) -> int:
        return self.__numberOfSeat - self.__numberOfEmptySeat

    def ratio(self) -> float:
        return self.numberOfBookedSeat()/ self.numberOfAllSeat()

    def turnover(self) -> int:
        return self.__turnover


