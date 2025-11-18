print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age=int(input("what is your age ? "))
if height >= 120:
    print("You can ride the rollercoaster")
    if age<12:
        print("child ticket is $5")
    elif age<18:
        print("youth ticket is $7")
    else:
        print("adult ticket is  $12")
else:
    print("Sorry you have to grow taller before you can ride.")
