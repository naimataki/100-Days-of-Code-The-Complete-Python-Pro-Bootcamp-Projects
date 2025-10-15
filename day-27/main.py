from tkinter import * 
import turtle

def button_clicked():
    print("I got clicked")
    #my_label["text"] = "Button Got Clicked"
    my_label.config(text=input.get())

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="I Am a Label!", font=("Ariel", 24, "bold"))
my_label["text"] = "New Text" #my_label.config(text="New Text")
my_label.grid(column=0, row=0)
#my_label.place(x=0, y=0)
#my_label.pack(side = "left")

#Button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
#button.pack()

#Entry

input = Entry(width = 10)
print(input.get())
input.grid(column=2, row=2)
#input.pack()


window.mainloop()