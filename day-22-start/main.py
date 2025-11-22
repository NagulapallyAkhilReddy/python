from turtle import Screen, Turtle

import paddle
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
game_is_on=False
user_input=pong_screen.textinput("start game","shall we start the game?: 'y' or 'n'")
if user_input.lower()=='y':
    game_is_on=True

while game_is_on:
    pong_screen.onkey(player1.move_up, "Up")
    pong_screen.onkey(player1.move_down, "Down")
    pong_screen.onkey(player2.move_up, "w")
    pong_screen.onkey(player2.move_down, "s")
    pong_screen.update()
    ball.forward(15)
    if ball.ycor()>=240 or ball.ycor()<=-240:
        ball.tiltangle(-ball.heading())








pong_screen.exitonclick()