import random
from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("white")
        self.up()
        self.setposition((random.randint(-360,360)),(random.randint(-230,230)))
        self.setheading(random.randint(1,360))
        self.speed(1)



# screen=Screen()
#
# ball1=Ball()
# ball1.setposition(0,5)
#
# screen.exitonclick()