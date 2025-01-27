from turtle import Turtle, Screen, colormode
from random import randint, choice, sample

colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.speed(0)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(360 / size_of_gap):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(10)

#timmy_the_turtle.circle(200)
for _ in range(72):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.circle(200, 5)

screen = Screen()
screen.exitonclick()