#with open("day-25/weather_data.csv") as csv_file:
#    data = csv_file.readlines()
#    print(data)

import csv
import pandas

with open("day-25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)