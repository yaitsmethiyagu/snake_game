from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.segment = Turtle("square")
        self.segment.color("white")
        self.segment.penup()

    def food_spawn(self):
        random_location = (random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))
        self.segment.setposition(random_location)
        #
        #     food = Turtle(shape="circle")
        #     food.penup()
        #
        #     food.color("white")
        #     food.setposition(random_location)
        #     return food
