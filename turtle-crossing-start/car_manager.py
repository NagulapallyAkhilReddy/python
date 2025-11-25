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
        self.shapesize(1,1.5)
        self.color(random.choice(COLORS))
        self.up()
        self.count=0
        self.setposition(350,random.randint(-240,250))
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE)

    def first_car(self):
         all_cars.append(self)
    def add_car(self):
        for x in range(len(all_cars)):
             if all_cars[x].distance(self)<40:
                 self.count+=1
        if self.count>=1:
            self.clear()
        else:
            all_cars.append(self)




    def move(self):
        for index in range(len(all_cars)):
            all_cars[index].forward(MOVE_INCREMENT)


    def no_hit(self,turtle_player):
        for index in range(len(all_cars)):
            if all_cars[index].distance(turtle_player)<21:
                return False
        return True
