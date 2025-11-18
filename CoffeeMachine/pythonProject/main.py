MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#check out the solution provided by mam in solution.py in Beginners pycharm course in 100 days of code
condition=True
money=0
def make_coffe(ingredients,cost):
    global money
    resources['water'] -= ingredients['water']
    resources['milk'] -= ingredients['milk']
    resources['coffee'] -= ingredients['coffee']
    money += cost
def process_coins():
    """Returns the total cost of the coins inserted"""
    print("please insert the coins")
    quaters=int(input("quaters: "))
    dimes=int(input("dimes : "))
    nickles=int(input("nickels : "))
    pennies=int(input("pennies : "))
    total=quaters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    return total
def check_resources(ingredients,cost):
    if ingredients['water'] <= resources['water'] and ingredients['milk'] <= resources['milk'] and ingredients['coffee'] <= resources['coffee']:
       cash=process_coins()
       if cash==cost:
           make_coffe(ingredients,cost)
           print(f"Here is your {user_input}. Enjoy!")

       elif cash>cost:
           make_coffe(ingredients, cost)
           change=round(cash-cost,2)
           print(f"Here is your {user_input}. Enjoy!\nand here is user ${change} dollars in change ")

       elif cash<cost:
           print(f"sorry that is not enough, money refunded ")

    elif ingredients['water']<resources['water']:
        print(f"sorry there is not enough water")
    elif ingredients['milk']<resources['milk']:
        print(f"sorry there is not enough milk")
    elif ingredients['coffee']<resources['coffee']:
        print(f"sorry there is not enough coffee")


while condition:
    #TODO: 1 - take the order
    #asking for the input
    user_input=input("What would you like today?(espresso/latte/cappuccino):").lower()
    #TODO: 2 - print the report of all the coffee machines
    if user_input=='report':
        for x in resources:
            if resources[x]=='coffee':
                print(x+":"+str(resources[x])+"mg")
            else:
                print(x+":"+str(resources[x])+"ml")

        print(f"money:${money}")

    #TODO: 3 - check resources sufficient
    espresso_ingredients=MENU["espresso"]["ingredients"]
    espresso_cost=MENU["espresso"]['cost']
    latte_ingredients=MENU["latte"]["ingredients"]
    latte_cost = MENU["latte"]['cost']
    cappuccino_ingredients=MENU["cappuccino"]["ingredients"]
    cappuccino_cost = MENU["cappuccino"]['cost']
    if user_input=='espresso':
        check_resources(espresso_ingredients,espresso_cost)
    elif user_input=='latte':
        check_resources(latte_ingredients,latte_cost)
    elif user_input=='cappuccino':
        check_resources(cappuccino_ingredients,cappuccino_cost)
    #TODO: 4 - process coins
    #TODO: 5 - check transaction successful
    #TODO; 6 - make coffee
    #TODO: 7 - turn off the coffee machine
    if user_input=='off':
        condition=False
        print("Thank you, I am switching to maintenance mode, will be back soon..")