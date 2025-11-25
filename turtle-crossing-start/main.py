import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#i have completed the whole project on my own
#and i saw mam's explanation, then i realised i have some few important to take into note
#after mam's explanation--- will update them

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
score=Scoreboard()
car1=CarManager()
car1.first_car()


shikamaru=Player()
screen.onkey(shikamaru.move,"Up")



game_is_on = True
while game_is_on:
    time.sleep(0.5-shikamaru.level_speed)
    car=CarManager()
    car.add_car()
    car.move()
    not_hit=car.no_hit(shikamaru)
    if shikamaru.ycor()>280:
        score.increase_level()
    if not not_hit:
        score.game_over()
        game_is_on=False

    screen.update()


screen.exitonclick()