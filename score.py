from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0

        self.penup()
        self.setposition(0, 280)
        self.color("white")
        self.hideturtle()
        self.write("Score: 0 ", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self, score):
        self.points += score
        self.clear()
        self.write(f"Score: {self.points} ", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
