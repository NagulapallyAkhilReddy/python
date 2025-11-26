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
raw_data={
    "names":["ajay","nihal","akhil"],
    "mode":["chillar","chillar pro max","decent"]
}
print(raw_data)
data_frame=pandas.DataFrame(raw_data)
print(data_frame)

data_frame.to_csv("dataframetocsv.csv")

