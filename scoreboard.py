from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 35, 'normal')

class Scoreboard(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.goto(x=x_cor, y=210)
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.display()

    def display(self):
        self.write(f"{self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self, text, x_cor):
        self.goto(x=x_cor, y=0)
        self.write(text, False, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.display()