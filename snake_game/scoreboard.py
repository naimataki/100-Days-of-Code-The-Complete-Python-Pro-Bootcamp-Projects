from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        #self.penup()
        #self.score = 0
        self.write("Score: 0")
        self.goto(0, 270)