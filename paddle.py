from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, player_num=1):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        if player_num == 1:
            self.goto(350, 0)
        if player_num == 2:
            self.goto(-350, 0)

    def move_up(self):
        self.forward(40)

    def move_down(self):
        self.backward(40)
