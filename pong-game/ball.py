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
