import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "US states game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("US states game/50_states.csv")
guessed_states = []
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt=f"{len(guessed_states)}/50 States Correct").title()
    #print(answer_state)
    
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        #print(missing_states)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer_state]
        t.goto(state.x.item(), state.y.item())
        t.write(state.state.item())  #t.write(answer_state)

#def get_mouse_click_coor(x, y):
#    print(x, y)
#
#turtle.onscreenclick(get_mouse_click_coor)
#
#turtle.mainloop()

screen.exitonclick()