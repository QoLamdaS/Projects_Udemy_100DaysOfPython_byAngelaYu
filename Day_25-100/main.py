import pandas
# import csv

# with open ("Day_25-100\\weather_data.csv") as csv_file:
#     data = csv_file.readlines()
#     print(data)

# with open ("Day_25-100\\weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)

data = pandas.read_csv("Day_25-100\\weather_data.csv")
print(data)
print(data["temp"])
