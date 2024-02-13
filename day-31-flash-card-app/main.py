from tkinter import *
from tkinter import messagebox
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

cards = data.to_dict(orient="records")

def generate_word():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    if len(cards) == 0:
        messagebox.showinfo(title="Victory", message="Congrats! You know all words")
        return

    current_card = random.choice(cards)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_lang, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, show_answer)

def answer_right():
    cards.remove(current_card)

    if len(cards) > 0:
        data_to_save = pandas.DataFrame(cards)
        data_to_save.to_csv("./data/words_to_learn.csv", index=False)
    else:
        if os.path.exists("./data/words_to_learn.csv"):
            os.remove("./data/words_to_learn.csv")

    generate_word()

def show_answer():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_lang, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

    window.after(3000, generate_word)


window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

# canvas with cards
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 265, image=card_front_img)
card_lang = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 265, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
button_right = Button(image=right_img, highlightthickness=0, command=answer_right)
button_right.grid(row=1, column=0)

button_wrong = Button(image=wrong_img, highlightthickness=0, command=generate_word)
button_wrong.grid(row=1, column=1)

flip_timer = window.after(3000, generate_word)
generate_word()


window.mainloop()