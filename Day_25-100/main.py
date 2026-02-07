import pandas

data = pandas.read_csv("Day_25-100\\weather_data.csv")
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)
print(data["temp"].mean())
print(data["temp"].max())
