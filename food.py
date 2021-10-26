import random
from turtle import Turtle, Screen
import time

FOOD_COLOR = "darkgreen"


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        food_xcor = random.randint(-240, 240)
        food_ycor = random.randint(-240, 240)
        self.goto(food_xcor, food_ycor)
        self.food_xcor = food_xcor
        self.food_ycor = food_ycor

    def food_eaten(self):
        self.penup()
        new_food_xcor = random.randint(-240, 240)
        new_food_ycor = random.randint(-240, 240)
        self.goto(new_food_xcor, new_food_ycor)
