from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEPS_FORWARD = 20


class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_part(position)

    def move(self):
        for part in range(len(self.parts) - 1, 0, -1):
            new_partx = self.parts[part - 1].xcor()
            new_party = self.parts[part - 1].ycor()
            self.parts[part].goto(new_partx, new_party)
        self.parts[0].forward(STEPS_FORWARD)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_snake_part(self, position):
        new_snake_part = Turtle("square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.goto(position)
        self.parts.append(new_snake_part)

    def extend(self):
        self.add_snake_part(self.parts[-1].position())
