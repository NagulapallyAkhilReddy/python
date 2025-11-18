from turtle import  Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shapesize(1,2)
        self.color("white")
        self.score=0
        self.up()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}",False,ALIGNMENT,FONT)

    def increase_score(self):
       self.clear()
       self.score+=1
       self.update_score()

    def game_over(self):
        self.home()
        self.write("Game Over",False,ALIGNMENT,FONT)
