from turtle import Turtle

ALLIGNMENT = 'center'
FONT = ('Courier', 18, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.color("Black")
        self.write(f"Score:{self.score} ", align=ALLIGNMENT, font=FONT)
        self.ht()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score} ", align=ALLIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALLIGNMENT, font=('Courier', 25, 'bold'))
