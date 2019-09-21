import json

with open('metro.json','r', encoding='cp1251') as f:
    metro_stations = json.loads(f.read())

for station in metro_stations:
    if station.get('RepairOfEscalators'):
        print(f"Ремонт эскалаторов на {station['NameOfStation']}")
