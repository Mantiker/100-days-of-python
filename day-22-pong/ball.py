from turtle import Turtle

class Ball(Turtle):
    def __init__(self, angle):
        super().__init__()

        self.angle = angle
        self.step = 10

        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.setheading(self.angle)

    def move(self):
        self.forward(self.step)

    def bounce_x(self):
        self.angle = 180 - self.angle # reverse on x axis
        self.setheading(self.angle)

    def bounce_y(self):
        self.angle *= -1 # reverse on y axis
        self.setheading(self.angle)

    def reset_position(self):
        self.bounce_x()
        self.bounce_y()
        self.goto(0, 0)
