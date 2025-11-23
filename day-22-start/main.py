from random import random
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle

pong_screen=Screen()
pong_screen.setup(800,500)
pong_screen.bgcolor("black")
# pong_screen.tracer(0)
pong_screen.listen()
player1=Paddle()
player1.setposition(380,0)
player2=Paddle()
player2.setposition(-380,0)
pong_screen.onkey(player1.move_up, "Up")
pong_screen.onkey(player1.move_down, "Down")
pong_screen.onkey(player2.move_up, "w")
pong_screen.onkey(player2.move_down, "s")

ball=Ball()

x=0
y=228
i=0




# pong_dash=[]
while y>-250:
    pong_dash_single=Turtle()
    pong_dash_single.color("white")
    pong_dash_single.shape("square")
    pong_dash_single.shapesize(1,0.2)
    # pong_dash[i].speed("slow")
    pong_dash_single.up()

    pong_dash_single.setposition(x,y)
    y = y - 30
    # pong_dash.append(pong_dash_single)
    i+=1
game_is_on=True



while game_is_on:
    # pong_screen.update()
    ball.forward(5)
    if ball.ycor()>=235 or ball.ycor()<=-230:
            ball.setheading(-ball.heading())

    if ball.distance(player1)<10 :
        if 0<=ball.heading()<=90:
            ball.setheading(ball.heading()+90)
        else:
            ball.setheading(ball.heading()-90)
    if ball.distance(player2)<10:
        if 180<=ball.heading()<=270:
            ball.setheading(ball.heading()+90)
        else:
            ball.setheading(ball.heading()-90)

    if ball.xcor()>400 or ball.xcor()<-400:
        game_is_on=False











pong_screen.exitonclick()