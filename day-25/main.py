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
# print(data["temp"])
data_dict=data.to_dict()
# print(data_dict)

temp_list=data["temp"].to_list()
# print(temp_list)
# sum=0
# for temp in temp_list:
#     sum+=temp
# avg=sum/len(temp_list)


# avg=sum(temp_list)/len(temp_list)
# print(avg)

#using series method
# avg=data["temp"].mean()
# print(avg)
#
# max_temp=data["temp"].max()
# print(max_temp)

#getting the row in which the temp is max
# print(data[data.temp==data.temp.max()])

#getting mondays temp as fahrenheit
monday=data[data.day=="Monday"]
# print(type(monday.temp))
# mon_temp=monday.temp[0]
# print(mon_temp*9/5+32)

#creating a dataframe from scratch
# raw_data={
#     "names":["ajay","nihal","akhil"],
#     "mode":["chillar","chillar pro max","decent"]
# }
# print(raw_data)
# data_frame=pandas.DataFrame(raw_data)
# print(data_frame)
#
# data_frame.to_csv("dataframetocsv.csv")

squirrel_data=pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
# # print(type(squirrel_data))
# count_grey=0---got confused a lot
# count_red=0---leave from here to the end of this continous comments
# count_black=0
# # print(squirrel_data.count(squirrel_data["Primary Fur Color"]=="Red"))
# # for row in squirrel_data:
# if "Gray" in squirrel_data["Primary Fur Color"] :
#     count_grey+=1
#     # if row["Primary Fur Color"]=="Red":
#     #     count_red+=1
#     # if row["Primary Fur Color"]=="Black":
#     #     count_black+=1
#
# print(count_grey) --- till here , leave it
squirrel_data=pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")

primary_fur_color=squirrel_data["Primary Fur Color"].to_list()
# print(primary_fur_color.count("Gray"))
# squirrel_by_primary_fur_color={"Gray":f"{primary_fur_color.count("Gray")}",
#                                "Red":f"{primary_fur_color.count("Cinnamon")}",
#                                "Black":f"{primary_fur_color.count("Black")}"}
squirrel_data=pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")

primary_fur_color=squirrel_data["Primary Fur Color"].to_list()
# print(primary_fur_color.count("Gray"))
# squirrel_by_primary_fur_color={"Gray":f"{primary_fur_color.count("Gray")}",
#                                "Red":f"{primary_fur_color.count("Cinnamon")}",
#                                "Black":f"{primary_fur_color.count("Black")}"}
squirrel_by_primary_fur_color={
    "colors":["Gray","Red","Black"],
    "count":[primary_fur_color.count("Gray"),primary_fur_color.count("Cinnamon"),primary_fur_color.count("Black")]
}
squirrel_by_primary_fur_color_dataframe=pandas.DataFrame(squirrel_by_primary_fur_color)
squirrel_by_primary_fur_color_dataframe.to_csv("squirrel_count_by_primary_fur_color.csv")







