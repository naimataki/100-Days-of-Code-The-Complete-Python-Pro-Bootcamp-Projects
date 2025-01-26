from turtle import Turtle, Screen
from random import randint

timmy_the_turtle = Turtle()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    timmy_the_turtle.color(r/255, g/255, b/255)



screen = Screen()
screen.exitonclick()
