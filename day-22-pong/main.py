from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p_right = Paddle((350, 0))
screen.listen()
screen.onkey(p_right.up, "Up")
screen.onkey(p_right.down, "Down")

p_left = Paddle((-350, 0))
screen.listen()
screen.onkey(p_left.up, "w")
screen.onkey(p_left.down, "s")

angle = random.randint(-70, 70)
ball = Ball(angle)

score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    ball.move()

    # detect collision with walls
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(p_right) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    # detect collision with left paddle
    if ball.distance(p_left) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # detect out of field
    if ball.xcor() < -400:
        ball.reset_position()
        score.increase_score_r()

    if ball.xcor() > 400:
        ball.reset_position()
        score.increase_score_l()

screen.exitonclick()