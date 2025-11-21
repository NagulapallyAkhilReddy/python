from turtle import Turtle
DISTANCE=30
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(90)
        self.up()
        self.speed("slow")
        self.shapesize(3, 0.4)


    def move_up(self):
       if  self.ycor()<210:
            self.goto(self.xcor() ,self.ycor()+DISTANCE)

    def move_down(self):
        if -210 < self.ycor():
            self.goto(self.xcor(),self.ycor()-DISTANCE)





