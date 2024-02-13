from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.r_score = 0
        self.l_score = 0

        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def increase_score_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_score_r(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Arial", 80, "normal"))
