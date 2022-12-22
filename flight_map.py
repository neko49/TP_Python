import csv
from typing import List

from flight import Flight
from airport import Airport

class FlightMap :
    def __init__(self):
        self.aeroports = []
        self.flight = []
    
    def import_airports(self, csv_file : str ) -> None:
        with open(csv_file, 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            for row in csv_reader:
                name, code, lat, long = row 
                airport = Airport(name, code, lat, long)
                self.aeroports.append(airport)
                
            
    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  
            for row in reader:
                src_code, dst_code, duration = row
                vol = Flight(src_code, dst_code, float(duration))
                self.flight.append(vol)
                
    def airports(self) -> List[Airport] :
        return self.aeroports
    
    def flights(self):
        return self.flight
    
    def airport_find(self, airport_code: str) -> Airport:
        for airport in self.aeroports:
            if airport.code == airport_code:
                return airport
            return None
    
    def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> Flight:
        for flight in self.flight:
            if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
                return True
            return False
    
    
 
    
        
        

                
    
            


