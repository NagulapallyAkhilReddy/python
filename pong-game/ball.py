from itertools import batched
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.speed(1)
        self.setposition(0,0)
        self.setheading(45)
        # self.goto(350,250)

    def move(self):
        new_x=self.xcor()+10
        new_y=self.ycor()+10
        self.goto(new_x,new_y)
