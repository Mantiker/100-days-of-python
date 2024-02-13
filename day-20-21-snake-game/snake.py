from turtle import Turtle

STEP = 20
STARTING_POSITIONS = [(0, 0), (-STEP, 0), (-2 * STEP, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for v in STARTING_POSITIONS:
            self.add_segment(v)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.shapesize(stretch_len=1, stretch_wid=1)
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        self.head.forward(STEP)
