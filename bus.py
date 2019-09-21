import csv

streets = {}

with open('bus_stops.csv', 'r', encoding='cp1251') as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        if row['Street'] in streets:
            streets[row['Street']] += 1
        else:
            streets[row['Street']] = 1

most_freq_stop = sorted(streets.items(), key = lambda item: item[1], reverse=True)[1]
print(f"Наиболее частая остановка {most_freq_stop[0]}")
