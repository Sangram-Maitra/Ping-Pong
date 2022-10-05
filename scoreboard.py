from turtle import Turtle

FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.goto(-180, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(180, 200)
        self.write(self.r_score, align="center", font=FONT)

    def left_score(self):
        self.clear()
        self.l_score += 1
        self.update()

    def right_score(self):
        self.clear()
        self.r_score += 1
        self.update()
