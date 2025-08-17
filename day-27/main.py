import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I Am a Label!", font=("Ariel", 24, "bold"))
my_label.pack(side="left", expand=True)

window.mainloop()