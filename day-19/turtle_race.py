from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
#print(user_bet)

if user_bet:
    is_race_on = True

turtles = []
for i in range(6):
        tim = Turtle(shape="turtle")
        tim.penup()
        tim.color(colors[i])
        tim.goto(x = -240, y = -100 + i*40)
        turtles.append(tim)

pace = randint(0, 10)
while is_race_on:
    for turtle in turtles:
        print(turtle.color)
        while turtle.xcor() != 230:
            turtle.forward(pace)

screen.exitonclick()
