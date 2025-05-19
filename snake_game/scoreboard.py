from turtle import Turtle

ALIGNNMENT = 'center'
FONT = ('Courier', 22, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNNMENT, font=FONT)

    def game_over(self):
        #self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNNMENT, font=FONT)