import random
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Classic Snake Game")
screen.bgcolor("cornsilk")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
# creating an object automatically calls the init function in that class. Hence snake will be created automatically.

screen.listen()
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_back)

game_is_on = True

while game_is_on:
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        scoreboard.update()
        food.food_eaten()
        snake.snake_grows()

        snake.move()

        screen.update()
        time.sleep(0.1)

    if snake.head.xcor() > 250 or snake.head.ycor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() < -250:
        game_is_on = False
        scoreboard.gameover()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()

    else:
        snake.move()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
