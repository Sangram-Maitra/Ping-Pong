from paddle import Paddle
from ball import Ball
from turtle import Screen
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.title("My Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 345 or ball.distance(l_paddle) < 50 and ball.xcor() < -345:
        ball.bounce_x()
        ball.increase_speed()

    if ball.xcor() > 390:
        scoreboard.left_score()
        ball.restart()

    if ball.xcor() < -390:
        scoreboard.right_score()
        ball.restart()

screen.exitonclick()
