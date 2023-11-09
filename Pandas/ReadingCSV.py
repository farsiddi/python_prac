# with open("weather_data.csv") as weather_data:
#     content = weather_data.readlines()
#     print(content)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     weather_data = csv.reader(weather_data)
#     temperature = []
#     for row in weather_data:
#         print(row)
#         if row[1] != "temp":  # Excluding label temp so that it can be converted into integer
#             temperature.append(int(row[1]))
# print(temperature)

# Just to take temp we have right above lines of code so that's why we use Pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data))  # This is a dataframe(rows and column)
print(data["temp"])  # Takes the first row as label and this is a series(a single column)
# print(data.temp)  Same as above lines
data_dict = data.to_dict()
print(
    data_dict)  # Coverts into dictionary where each column is itself is a dictionary and all the columns(dictionaries) are nested inside another dictionary
data_list = data["temp"].to_list()
print(data_list)
# sum = 0
# for n in data_list:
#     sum += n
# average_temp = round(sum / len(data_list), 2)
# print(average_temp)
print(round(sum(data_list) / len(data), 2))

print(data["temp"].mean())  # Working with Series in Pandas
maximum_temp = data["temp"].max()
print(maximum_temp)

# Getting a row
print(data[data.day == "Monday"])

# Getting a row having the maximum data
print(data[data.temp == data["temp"].max()])  # After == we are filtering the data according the given condition

monday = data[data.day == "Monday"]
print(monday.condition)