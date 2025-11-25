import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
score=Scoreboard()


shikamaru=Player()
screen.onkey(shikamaru.move,"Up")



game_is_on = True
while game_is_on:
    time.sleep(0.5-shikamaru.level_speed)
    car=CarManager()
    car.move()
    game_is_on=car.hit(shikamaru)
    if shikamaru.ycor()>280:
        score.increase_level()
    if not game_is_on:
        score.game_over()

    screen.update()


screen.exitonclick()