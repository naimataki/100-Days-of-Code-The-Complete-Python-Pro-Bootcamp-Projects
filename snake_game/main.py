from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

snake = []
for i in range(3):
    tim = Turtle("square")
    tim.penup()
    tim.color("white")
    tim.setx(-20*i)
    snake.append(tim)

game_is_on = True
while game_is_on:
    for segment in snake:
        segment.forward(20)

screen.exitonclick()