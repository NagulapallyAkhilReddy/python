import random
import turtle
from turtle import Screen
y_value=-100
colors=["red","orange","brown","violet","blue"]
turtles=[]

racing_platform=Screen()
racing_platform.setup(500,400)

is_game_on=False
# def random_color():
#     choice_color=random.choice(colors)
#     colors.remove(choice_color)
#     return choice_color
for index in range(5):
    my_turtle=turtle.Turtle(shape="turtle")
    my_turtle.color(colors[index])
    my_turtle.up()
    my_turtle.goto(x=-230,y=y_value)
    turtles.append(my_turtle)
    y_value+=50


is_user_input=True
user_bet=""
while is_user_input:
    user_bet=racing_platform.textinput("what's your bet","Which turtle will win the race? Enter a color : ")
    print(user_bet)
    if user_bet in colors:
        is_user_input = False
        is_game_on=True
    # else:
    #     print("enter valid color")

x=0
while is_game_on:
    for racer in turtles:
        if racer.xcor()>230:
            is_game_on=False
            if user_bet==racer:
                print(f"you won, the winner is {racer.pencolor()}")
            else:
                print(f"you lost, the winner is {racer.pencolor()}")
        racer.speed(100)
        racer.forward(random.randint(1, 10))




racing_platform.exitonclick()


