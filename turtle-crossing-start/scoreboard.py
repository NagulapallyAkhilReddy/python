from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.up()
        self.hideturtle()
        self.setposition(-260,260)
        self.increase_level()

    def increase_level(self):
        self.level+=1
        self.write("level : "+str(self.level),align="left",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)


