# with open("./weather_data.csv") as f:
#     data = f.readlines()
#
# print(data)

# import csv
#
# with open("./weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
print(data.to_csv())
print(data["temp"].to_list())

print(len(data["temp"]))
print(data["temp"].mean())
print(data["temp"].max())

# Get data in Columns
print(data["condition"])
print(data.condition)

#Get data in Rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_farenheit = monday_temp * 9 / 5 + 32
print(monday_temp_farenheit)


# Create Dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("./new_data.csv")