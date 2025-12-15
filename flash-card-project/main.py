from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("flash-card-project/data/french_words.csv")
to_learn = data.to_dict(orient="records")
#print(to_learn)
#print(data)

def next_card():
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"])

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="flash-card-project/images/card_front.png")
canvas.create_image(400, 263, image=front_card)
language_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="flash-card-project/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="flash-card-project/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

window.mainloop()

