import pandas

data = pandas.read_csv("Day_25-100\\The Great Squirrel Census Data Analysis in Lecture 192\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
squirrels_csv_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
the_data_frame = pandas.DataFrame(squirrels_csv_dict)
the_data_frame.to_csv("Day_25-100\\The Great Squirrel Census Data Analysis in Lecture 192\\final_squirrel_count.csv")

