from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# game environment setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.display_score()

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for part in snake.parts[1:]:
        if snake.head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
