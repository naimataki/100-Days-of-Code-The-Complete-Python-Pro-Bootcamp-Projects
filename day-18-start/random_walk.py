from turtle import Turtle, Screen, colormode
from random import randint, choice, sample

colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed(0)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)
    #timmy_the_turtle.color(r/255, g/255, b/255)

#move_1 = [timmy_the_turtle.forward, timmy_the_turtle.backward]
#move_2 = [timmy_the_turtle.right, timmy_the_turtle.left]
#
#for _ in range(200):
#    random_color()
#    choice(move_1)(30)
#    choice(move_2)(90)

directions = [0, 90, 180, 270]

for _ in range(200):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(choice(directions))

screen = Screen()
screen.exitonclick()
