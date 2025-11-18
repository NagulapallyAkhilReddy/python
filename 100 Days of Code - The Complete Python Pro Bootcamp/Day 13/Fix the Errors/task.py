try:
    age = int(input("How old are you?"))
except ValueError:
    print("you have entered an invalid number, please enter a valid numerical value such as 12.")
    age=int(input("how old are u? : "))
if age > 18:
    print(f"You can drive at age {age}.")
