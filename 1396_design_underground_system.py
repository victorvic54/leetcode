class UndergroundSystem:
    def __init__(self):
        self.checkin = {}
        self.average_station = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkin[id]
        
        average_time, number_of_stations = 0, 0
        if (start_station, stationName) in self.average_station:
            average_time, number_of_stations = self.average_station[(start_station, stationName)]

        updated_average_time = ((average_time * number_of_stations) + (t - start_time)) / (number_of_stations + 1)
        self.average_station[(start_station, stationName)] = (updated_average_time, number_of_stations + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.average_station[(startStation, endStation)][0]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
