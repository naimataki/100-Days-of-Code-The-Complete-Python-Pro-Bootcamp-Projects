from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_clockwise():
    tim.setheading(tim.heading() + 10)
def move_counterclockwise():
    tim.setheading(tim.heading() - 10)
def clear():
    tim.setpos(0, 0)
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="d", fun=move_counterclockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

