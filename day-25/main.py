# with open("weather_data.csv") as weather_data:
#     report=weather_data.readlines()
#     print(report)

# import csv
# with open("weather_data.csv") as weather_data:
#     data=csv.reader(weather_data)
#     temperature=[]
#     for row in data:
        # if row[1]!="temp":#easy and fast way
        #     temperature.append(int(row[1]))

        #a bit long code--on first try
    #     temperature.append(row[1])
    # temperature=temperature[1:]
    # i=0
    # for temp in temperature:
    #     temperature[i]=int(temp)
    #     i+=1
    # print(temperature)

import pandas
data=pandas.read_csv("weather_data.csv")
print(data["temp"])