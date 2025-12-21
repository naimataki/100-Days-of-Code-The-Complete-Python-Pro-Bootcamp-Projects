from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("flash-card-project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("flash-card-project/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:    
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    #print(current_card["French"])
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("flash-card-project/data/words_to_learn.csv", index=False) 

    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="flash-card-project/images/card_front.png")
back_card = PhotoImage(file="flash-card-project/images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card)
language_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="flash-card-project/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="flash-card-project/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()

