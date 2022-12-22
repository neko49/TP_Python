import csv

from flight import Flight
from airport import Airport

class FlightMap :
    def __init__(self):
        self.aeroports = [Airport]
        self.flight = [Flight]
    
    def import_airports(self, csv_file : str ):
        import csv
        with open(csv_file, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=' ')
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
                
    def airports(self):
        return self.aeroports
    
    def flights(self):
        return self.flight
    
    

    
    
        
        

                
    
            


