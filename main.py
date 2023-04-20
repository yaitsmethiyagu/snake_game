from snake import Snake
from turtle import Screen
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

SPEED = 0.3

food = Food()
snake = Snake()
score = Score()
WALL_H = 290
is_on = True

screen.listen()
screen.onkey(fun=snake.turn_up, key="Up")
screen.onkey(fun=snake.turn_down, key="Down")
screen.onkey(fun=snake.turn_left, key="Left")
screen.onkey(fun=snake.turn_right, key="Right")

while is_on:

    screen.update()
    time.sleep(SPEED)
    snake.snake_move()
    screen.update()

    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 15:
            score.reset_score()
            snake.reset_snake()
            time.sleep(1)
            # is_on = False

    if snake.snake_head.distance(food) < 10:
        food.food_spawn()
        snake.grow_body()
        score.update_score(1)

    if snake.snake_head.xcor() < -WALL_H or snake.snake_head.xcor() > WALL_H or snake.snake_head.ycor() > WALL_H or snake.snake_head.ycor() < -WALL_H:
        score.reset_score()
        snake.reset_snake()
        time.sleep(1)
        # is_on = False

screen.exitonclick()
