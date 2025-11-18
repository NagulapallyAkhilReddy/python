import turtle
from turtle import Screen



def move_forward():
    jhonny.forward(30)
jhonny=turtle.Turtle()
my_screen=Screen()
my_screen.listen()
my_screen.onkey(key="space",fun=move_forward)
my_screen.exitonclick()