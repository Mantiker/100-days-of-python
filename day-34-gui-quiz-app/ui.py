from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR,  font=("Arial", 16))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        button_true_img = PhotoImage(file="./images/true.png")
        self.button_true = Button(width=100, image=button_true_img, highlightthickness=0, command=self.correct_answer)
        self.button_true.grid(row=2, column=0)

        button_false_img = PhotoImage(file="./images/false.png")
        self.button_false = Button(width=100, image=button_false_img, highlightthickness=0, command=self.wrong_answer)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.game_over()

    def correct_answer(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        self.window.after(500, self.get_next_question)

    def wrong_answer(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        self.window.after(500, self.get_next_question)

    def give_feedback(self, is_right: bool):
        color = "red"
        if is_right:
           color = "green"

        self.canvas.config(bg=color)

    def game_over(self):
        self.canvas.itemconfig(self.question_text, text="You have finished quiz")
        self.button_true.config(state="disabled")
        self.button_false.config(state="disabled")