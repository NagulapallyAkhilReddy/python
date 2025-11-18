import turtle
from turtle import Screen
import time

platform=Screen()
platform.setup(width=600,height=600)
platform.bgcolor("black")
# x=0
# for _ in range(3):
#     my_snake=turtle.Turtle()
#     my_snake.up()
#     my_snake.color("white")
#     my_snake.shape("square")
#     x-=20
#     my_snake.setposition(x,0)

#after mam's explanation
starting_positions=[(0,0),(-20,0),(-40,0)]
my_snake=[]

for position in starting_positions:
    my_snake_part=turtle.Turtle("square")
    my_snake_part.color("white")
    my_snake_part.shape("square")
    my_snake_part.up()
    my_snake_part.setposition(position)

    my_snake.append(my_snake_part)


lets_play=True
while lets_play:
    for index in range(len(my_snake)-1,0,-1):
        x=my_snake[index-1].xcor()
        y=my_snake[index-1].ycor()
        my_snake[index].goto(x,y)
        turtle.update()
    time.sleep(0.1)
    my_snake[0].left(90)
    my_snake[0].forward(20)

platform.exitonclick()