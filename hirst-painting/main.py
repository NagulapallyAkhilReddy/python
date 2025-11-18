import turtle
import random
from turtle import Screen

import colorgram

# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     r_color=(r,g,b)
#     return r_color


turtle.colormode(255)
colors=colorgram.extract('hirstpainting.jpg',10)
colorslist=[]
for x in colors:
    r=x.rgb.r
    b=x.rgb.b
    g=x.rgb.g
    colorslist.append((r,b,g))

jhonny_the_turtle=turtle.Turtle()
y=0
x=0
jhonny_the_turtle.up()
jhonny_the_turtle.setposition(-350,-350)
for _ in range(10):
    for _ in range(10):
        jhonny_the_turtle.dot(20,random.choice(colorslist))
        jhonny_the_turtle.up()
        jhonny_the_turtle.forward(50)
        (x,y)=(jhonny_the_turtle.pos())
    jhonny_the_turtle.up()
    jhonny_the_turtle.setposition(-350, y + 50)


my_screen=Screen()

my_screen.exitonclick()
