from turtle import Turtle

DISTANCE = 20


class Snake:

    def __init__(self):
        self.segment = Turtle("square")
        self.segment.color("white")
        self.segment.penup()
        self.snake_body = [self.segment]
        self.grow_body()
        self.grow_body()
        self.grow_body()
        # self.grow_body()
        # self.grow_body()
        # self.grow_body()
        # self.grow_body()
        self.snake_head = self.snake_body[0]

    def grow_body(self):
        self.snake_body.append(Turtle("square"))
        last_segment = self.snake_body[-1]
        last_segment.color("white")
        last_segment.penup()
        previous_segment = self.snake_body[-2]
        last_segment.setposition(previous_segment.position()[0] - 20, previous_segment.position()[1])

    def snake_move(self):

        for i in range(len(self.snake_body) - 1, 0, -1):
            last_segment = self.snake_body[i]
            previous_segment = self.snake_body[i - 1]
            last_segment.setposition(previous_segment.xcor(), previous_segment.ycor())
            # screen.update()
        self.snake_head.forward(DISTANCE)

    def turn_up(self):
        if self.snake_head.heading() != 90 * 3:
            self.snake_head.setheading(90 * 1)

    def turn_down(self):
        if self.snake_head.heading() != 90 * 1:
            self.snake_head.setheading(90 * 3)

    def turn_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(90 * 2)

    def turn_right(self):
        if self.snake_head.heading() != 90 * 2:
            self.snake_head.setheading(90 * 0)
