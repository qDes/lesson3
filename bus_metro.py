import csv 
import json
from datetime import datetime
from math import radians, cos, sin, asin, sqrt




def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

def get_metro_crd(station):
    try:
        lon = float(station['Longitude_WGS84'])
        lat = float(station['Latitude_WGS84'])
        return lon, lat
    except ValueError:
        return 0,0

def get_bus_crd(bus):
    try:
        lon = float(bus['Longitude_WGS84'])
        lat = float(bus['Latitude_WGS84'])
        return lon, lat
    except ValueError:
        return 0, 0

if __name__ == '__main__':
    start_time = datetime.now()
    bus_stops = []
    station_stops = dict()
    count = 0
    with open('bus_stops.csv','r', encoding='cp1251') as f:
        reader = csv.DictReader(f,delimiter=';')
        for row in reader:
            bus_stops.append(row)

    with open('metro.json','r', encoding='cp1251') as f:
        metro_stations = json.loads(f.read())


    for station in metro_stations:
        name = station['NameOfStation']
        station_stops[name] = 0
        for stop in bus_stops: 
            lon1,lat1 = get_metro_crd(stop)
            lon2,lat2 = get_bus_crd(station)
            distance = haversine(lon1,lat1, lon2, lat2)
            count += 1
            if distance <= 0.5:
                station_stops[name] += 1 

    target_station = max(station_stops, key=station_stops.get)
    exec_time = datetime.now() - start_time
    print(f"Number of operations {count}.")
    print(f"Execution time {exec_time}.")
    print(f"Станция {target_station} имеет наибольшее количество автобусных остановок в радиусе 0.5 км.")
