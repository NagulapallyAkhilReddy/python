import random
import turtle
from turtle import Turtle, Screen

jhonny_the_turtle=Turtle()
jhonny_the_turtle.shape("turtle")
jhonny_the_turtle.color("orange")
#turtle challenge 1
# jhonny_the_turtle.forward(100)
# jhonny_the_turtle.right(90)
# jhonny_the_turtle.forward(100)
# jhonny_the_turtle.right(90)
# jhonny_the_turtle.forward(100)
# jhonny_the_turtle.right(90)
# jhonny_the_turtle.forward(100)

# turtle challenge 2
# for _ in range(15):
#     jhonny_the_turtle.forward(10)
#     jhonny_the_turtle.up()
#     jhonny_the_turtle.forward(10)
#     jhonny_the_turtle.down()

#turtle challenge 3
# mam did this in more organnized way, using fuctions
#but i like mine better
# turtle.colormode(255)
# for x in range(3,11):
#     r=random.randint(0,255)
#     b=random.randint(0,255)
#     g=random.randint(0,255)
#     jhonny_the_turtle.color(r,b,g)
#     for s in range(x):
#         jhonny_the_turtle.forward(100)
#         jhonny_the_turtle.right(360/x)


# mam's version'
#a bit better one, i modified it
# turtle.colormode(255)
# def draw_shape(x):
#     for s in range(x):
#         jhonny_the_turtle.forward(100)
#         jhonny_the_turtle.right(360/x)
#
# for x in range(3,11):
#     r=random.randint(0,255)
#     b=random.randint(0,255)
#     g=random.randint(0,255)
#     jhonny_the_turtle.color(r,b,g)
#     draw_shape(x)

#turtle challenge 4
turtle.colormode(255)
# for x in range(200):
#     r = random.randint(0, 255)
#     b=random.randint(0,255)
#     g=random.randint(0,255)
#     jhonny_the_turtle.color(r,b,g)
#
#     jhonny_the_turtle.width(15)
#     jhonny_the_turtle.speed(20)
#     jhonny_the_turtle.forward(50)
    # x=random.randint(0,1)
    # if x==0:
    #     jhonny_the_turtle.right(90)
    # if x==1:
    #     jhonny_the_turtle.left(90)
    # y = random.choice([0,90,180,270])
    # jhonny_the_turtle.right(y)

#turtle challenge 5
def random_color():
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    r_color=(r,b,g)#tuple
    return r_color
angle=0
while angle<360:
    jhonny_the_turtle.color(random_color())
    jhonny_the_turtle.speed(50)
    jhonny_the_turtle.circle(50)
    jhonny_the_turtle.right(5)
    angle+=5



my_screen=Screen()

my_screen.exitonclick()