from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
#def timer_reset():
#    print("I got clicked")
#    canvas.config(text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    print(count)
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)
count_down(5)

title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"))
title_label.config(fg=GREEN, bg=YELLOW, highlightthickness=0)
title_label.grid(column=1, row=0)

start_button = Button(text="Start")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_label = Label(text="✔️", font=(FONT_NAME, 20, "bold"))
check_label.config(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_label.grid(column=1, row=3)

window.mainloop()