from turtle import Screen
from paddle import  Paddle
from scoreboard import Scoreboard
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong Game')
screen.tracer(0)
screen.listen()
paddle_1 = Paddle(player_num=1)
paddle_2 = Paddle(player_num=2)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=paddle_1.move_up)
screen.onkey(key="Down", fun=paddle_1.move_down)
screen.onkey(key="w", fun=paddle_2.move_up)
screen.onkey(key="s", fun=paddle_2.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')
    if ball.xcor() > 320 and ball.distance(paddle_1) < 50 :
        ball.bounce('x')
    if ball.xcor() < -320 and ball.distance(paddle_2) < 50:
        ball.bounce('x')

    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()
