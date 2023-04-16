import random
from snake import Snake
from turtle import Screen
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
food.food_spawn()
while True:
    snake.snake_move()
    screen.update()
    time.sleep(.5)

    screen.onkey(fun=snake.turn_up, key="Up")
    screen.onkey(fun=snake.turn_down, key="Down")
    screen.onkey(fun=snake.turn_left, key="Left")
    screen.onkey(fun=snake.turn_right, key="Right")

# def food_spawn():
#     random_location = (random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))
#
#     food = Turtle(shape="circle")
#     food.penup()
#
#     food.color("white")
#     food.setposition(random_location)
#     return food


# def eat_food(food):
#     if turtle_body[len(turtle_body) - 1].position() == food.position():
#         print("met")
#         print(food.position())
#         print(turtle_body[len(turtle_body) - 1].position())
#         grow_body()
#         food.clear()
#     print(f"{food.position()} food ")
#     print(f"{turtle_body[len(turtle_body) - 1].position()} tutrle")


# is_game_on = True
# food = food_spawn()


#
#

screen.exitonclick()
