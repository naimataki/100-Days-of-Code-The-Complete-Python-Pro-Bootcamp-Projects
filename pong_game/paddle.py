from turtle import Turtle
WIDTH = 20
HEIGHT = 20
XPOS = 350
YPOS = 0
UP = 90
DOWN = 270

class Paddle:

    def __init__(self):
        paddle = Turtle("square")
        paddle.shapesize(WIDTH, HEIGHT)
        paddle.color("white")
        paddle.penup()
        paddle.goto((XPOS, YPOS))