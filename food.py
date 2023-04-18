from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("blue")
        self.food_spawn()

    def food_spawn(self):
        random_location = (random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))
        self.setposition(random_location)
