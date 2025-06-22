from turtle import Turtle
#WIDTH = 20
#HEIGHT = 20
UP = 0
DOWN = 180
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        #self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        #self.showturtle()


    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)