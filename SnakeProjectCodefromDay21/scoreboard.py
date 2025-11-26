from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("../../OneDrive/Desktop/scorefile.txt") as score_file:
            the_highscore=int(score_file.read())
        self.score = 0
        self.highscore=the_highscore
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        with open("../../OneDrive/Desktop/scorefile.txt",mode="w") as score_file:
            score_file.write(f"{self.highscore}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def reset_game(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
