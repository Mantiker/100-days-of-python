from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("blue")
        self.refresh()

    def refresh(self):
        x = random.randint(-15, 14) * 20 + 10
        y = random.randint(-15, 14) * 20 + 10
        self.goto(x, y)
