from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.title_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.title_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 
                                                     125, 
                                                     width=280, 
                                                     text="goes here", 
                                                     fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_image = PhotoImage(file="quizzler-app/images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0)
        self.right_button.grid(column=0, row=2)

        wrong_image = PhotoImage(file="quizzler-app/images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_qustion()

        self.window.mainloop()

    def get_next_qustion(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)