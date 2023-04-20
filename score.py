from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = 0
        self.read_high_score()

        self.penup()
        self.setposition(0, 280)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.points} | High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self, score):
        self.points += score
        self.clear()
        self.write(f"Score: {self.points} | High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.points > self.high_score:
            self.high_score = self.points
            self.write_high_score(self.high_score)
        self.points = 0
        self.update_score(0)

    def read_high_score(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())


    def write_high_score(self, score):
        with open("data.txt", mode="w") as file:
            file.write(str(score))




