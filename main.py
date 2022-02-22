from turtle import Screen
from paddle import  Paddle
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

screen.onkey(key="Up", fun=paddle_1.move_up)
screen.onkey(key="Down", fun=paddle_1.move_down)
screen.onkey(key="w", fun=paddle_2.move_up)
screen.onkey(key="s", fun=paddle_2.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()



screen.exitonclick()
