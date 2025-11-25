from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="flash-card-project/images/card_front.png")
canvas.create_image(400, 263, image=front_card)
language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="flash-card-project/images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="flash-card-project/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

window.mainloop()

