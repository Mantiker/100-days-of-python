from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput("Choose the winner", "Pick the color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
for i in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-230, -75 + i * 30)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if user_bet == winning_color:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")

        r = random.randint(0, 10)
        turtle.forward(r)

screen.exitonclick()