from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    #messagebox.showinfo(title="Title", message="Message")
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                           f"\nPassword: {password} \nIs it ok to save?")
    
    if is_ok:
        with open("password-manager/data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)  


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="password-manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width = 50)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input = Entry(width = 50)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "takioutinaima10@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width = 32)
password_input.grid(column=1, row=3)

password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()