import time
from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.setposition(STARTING_POSITION)
        self.setheading(90)
        self.level_speed=0

    # def increase_level(self):


    def move(self):
        if self.ycor()<280:
            self.forward(MOVE_DISTANCE)

        if self.ycor()>=280:
            time.sleep(1)
            self.level_speed=0.1
            self.setposition(STARTING_POSITION)


