from turtle import Turtle, Screen
from random import randint, choice, sample

timmy_the_turtle = Turtle()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    timmy_the_turtle.color(r/255, g/255, b/255)

move_1 = [timmy_the_turtle.forward, timmy_the_turtle.backward]
move_2 = [timmy_the_turtle.right, timmy_the_turtle.left]

for _ in range(100):
    random_color()
    choice(move_1)(30)
    choice(move_2)(90)

screen = Screen()
screen.exitonclick()
