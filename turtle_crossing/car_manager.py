from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#naimataki

class CarManager(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.color(choice(COLORS))
        self.penup()
        self.setheading(90)
        self.setx(320) 
        self.sety(randint(-250, 250)) 
        self.move_speed = 0.1
        self.forward(STARTING_MOVE_DISTANCE)