from turtle import Screen
from paddle import  Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong Game')
screen.listen()
paddle = Paddle()
screen.onkey(key="Up", fun=paddle.move_up)
screen.onkey(key="Down", fun=paddle.move_down)



screen.exitonclick()
