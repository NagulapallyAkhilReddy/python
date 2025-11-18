# print("welcome to the tip calculator")
# bill=float(input("what was the total bill ? "))
# tip=int(input("how much tip would you like to give ? "))
# people=int(input("how many people are you ? "))
# cost=(bill+(bill*tip)/100)/people
# amount=round(cost,2)
# print(f"each person would have to pay {amount}")
print("welcome to tip calculator!")
bill=int(input("what was the total bill?\n"))
tip=int(input("how much tip would u like to give (%)?\n"))
no_of_people=int(input("how many people to split the bill?\n"))
tip_amount=(tip/100)*bill
amount_for_each_person=(bill+tip_amount)/no_of_people
print(f"Each person should pay {round(amount_for_each_person,2)}")


