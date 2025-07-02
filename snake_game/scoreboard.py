from turtle import Turtle

ALIGNNMENT = 'center'
FONT = ('Courier', 22, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("snake_game/data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game/data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
    #    #self.clear()
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNNMENT, font=FONT)

    def increase_score(self):
        #self.clear()
        self.score += 1
        self.update_scoreboard()