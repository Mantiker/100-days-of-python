import time
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
MILLISECONDS_IN_ONE_SECOND = 1000
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checker_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        title_label.config(text="Rest", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = int(count / 60)
    sec = count % 60
    if min < 10:
        min = f"0{min}"
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")

    if count > 0:
        global timer
        timer = window.after(MILLISECONDS_IN_ONE_SECOND, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(int(reps/2)):
            mark += "✔"
            checker_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=120, pady=80, bg=YELLOW)

#canvas
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

# labels
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 26, "bold"))
title_label.grid(column=1, row=0)

checker_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, "bold"))
checker_label.grid(column=1, row=3)

# buttons
start_button = Button(text="Start", font=(FONT_NAME, 16, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 16, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
