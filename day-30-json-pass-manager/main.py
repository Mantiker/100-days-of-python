from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    pass_input.delete(0, END)
    pass_input.insert(END, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showerror(title="Error", message="All fields must be filled in")
        return

    try:
        with open("./passwords.json", mode="r") as f:
            d = json.load(f)
    except FileNotFoundError:
        with open("./passwords.json", mode="w") as f:
            json.dump(new_data, f, indent=2)
    else:
        d.update(new_data)
        with open("./passwords.json", mode="w") as f:
            json.dump(d, f, indent=2)
    finally:
        website_input.delete(0, END)
        pass_input.delete(0, END)

# ---------------------------- SEARCH WEBSITE ------------------------- #
def search_website():
    website = website_input.get()

    try:
        with open("./passwords.json", mode="r") as f:
            d = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"The data file is empty")
    else:
        if website in d:
            got_email = d[website]["email"]
            got_password = d[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {got_email}\nPassword: {got_password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for website: {website}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=202, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# 1 row
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=25)
website_input.grid(row=1, column=1)
website_input.focus()

website_button = Button(width=16, text="Search", command=search_website)
website_button.grid(row=1, column=2)

# 2 row
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=45)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "angela@gmail.com")

# 3 row
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_input = Entry(width=25)
pass_input.grid(row=3, column=1)

pass_generate_button = Button(text="Generate Password", command=generate_pass)
pass_generate_button.grid(row=3, column=2)

# 4 row
add_button = Button(width=40, text="Add", command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()