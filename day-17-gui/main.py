import random
from turtle import Screen, Turtle

timmy = Turtle()

# square
# timmy.goto(0, -100)
# timmy.goto(-100, -100)
# timmy.goto(-100, 0)
# timmy.goto(0, 0)

# dash line
# step = 10
# for i in range (20):
#     timmy.penup()
#     timmy.forward(step)
#     timmy.pendown()
#     timmy.forward(step)

# from triangle to pentagon
for i in range(3, 11):
    angle = 360 / i
    timmy.color = random.randint(0, 255)

    for _ in range(i):
        timmy.right(angle)
        timmy.forward(100)


screen = Screen()
screen.exitonclick()