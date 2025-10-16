from tkinter import * 

def button_clicked():
    print("I got clicked")
    label3.config(text=f"{float(input.get()) * 1.6}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=125)
window.config(padx=20, pady=30)

#Entry

input = Entry(width = 10)
input.insert(END, string="0")
print(input.get())
input.grid(column=1, row=0)


#Labels
label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label1.config(padx=10)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label2.config(padx=10)

label3 = Label(text="Km")
label3.grid(column=2, row=1)
label3.config(padx=10)

label3 = Label(text="0")
label3.grid(column=1, row=1)

new_button = Button(text="Calculate", command=button_clicked)
new_button.grid(column=1, row=2)

window.mainloop()