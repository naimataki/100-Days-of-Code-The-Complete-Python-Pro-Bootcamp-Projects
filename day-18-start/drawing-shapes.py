from turtle import Turtle, Screen
from random import randint

timmy_the_turtle = Turtle()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    timmy_the_turtle.color(r/255, g/255, b/255)

def draw_shape(sides_number):
    random_color()
    for _ in range(sides_number):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(360 / sides_number)

for n in range(3, 11):
    draw_shape(n)


screen = Screen()
screen.exitonclick()