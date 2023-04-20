import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.random_x = None
        self.random_y = None
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-280, 280)
        self.random_y = random.randint(-280, 280)
        self.goto(self.random_x, self.random_y)
