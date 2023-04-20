from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.score = 0

    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score = self.score + 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

