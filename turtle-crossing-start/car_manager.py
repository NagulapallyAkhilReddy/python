import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
all_cars=[]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.up()
        self.setposition(300,random.randint(-280,280))
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE)
        all_cars.append(self)



    def move(self):
        for index in range(len(all_cars)):
            all_cars[index].forward(MOVE_INCREMENT)


    def hit(self,turtle_player):
        for index in range(len(all_cars)):
            if all_cars[index].distance(turtle_player)<30:
                return False
        return True
