import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)



r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_down,"s")

ball=Ball()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.speed(0.2)
    ball.goto(350,250)




screen.exitonclick()