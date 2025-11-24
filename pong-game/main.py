import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Score

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)




r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
screen.listen()
score=Score()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    #detect collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect the collision with the paddle
    if ball.xcor()>320 and ball.distance(r_paddle)<50 or ball.xcor()<-320 and ball.distance(l_paddle)<50:
        ball.bounce_x()

    #detect when the paddle misses the ball
    if ball.xcor()>400:
        score.l_point()
        time.sleep(0.1)
        ball.setposition(0,0)
        ball.ball_speed=0.1
        ball.bounce_x()
        ball.bounce_y()

    if ball.xcor()<-400:
        score.r_point()
        time.sleep(0.1)
        ball.setposition(0,0)
        ball.ball_speed=0.1
        ball.bounce_x()
        # ball.bounce_y()




screen.exitonclick()