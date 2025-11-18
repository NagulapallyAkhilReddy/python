from turtle import  Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shapesize(1,2)
        self.color("white")
        self.up()
        self.goto(0, 300)
        self.update_score(0)

    def update_score(self,score):
        self.write(f"Score : {score}",False,"center",("Arial",8,"normal"))
