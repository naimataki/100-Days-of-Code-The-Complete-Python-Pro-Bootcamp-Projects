#with open("day-25/weather_data.csv") as csv_file:
#    data = csv_file.readlines()
#    print(data)

#import csv

#with open("day-25/weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

data = pandas.read_csv("day-25/weather_data.csv")
#print(type(data))
#print(data['temp'])
#print(data)

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data['temp'].to_list()
#print(len(temp_list))
#print(sum(temp_list) / len(temp_list))

#print(data['temp'].mean())
#print(data['temp'].max())

#get data in columns

#print(data["condition"])
#print(data.condition)

#get data in rows

#max_temp = data.temp.max()
#print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
#print(monday.condition)

monday_temp = monday.temp[0]
monday_temp_F = monday_temp * (9 / 5) + 32
print(monday_temp_F)

#Create a dataframe from scratch

data_dict = {
    "students": ["Naima", "Reda", "Najiba"],
    "scores": [76, 56, 65]
}