from turtle import Screen
from paddle import  Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong Game')
screen.tracer(0)
screen.listen()
paddle1 = Paddle(player_num=1)
paddle2 = Paddle(player_num=2)

screen.onkey(key="Up", fun=paddle1.move_up)
screen.onkey(key="Down", fun=paddle1.move_down)
screen.onkey(key="w", fun=paddle2.move_up)
screen.onkey(key="s", fun=paddle2.move_down)

game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()
