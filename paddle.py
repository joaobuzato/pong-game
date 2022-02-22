from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.goto(350, 0)

    def move_up(self):
        self.forward(40)

    def move_down(self):
        self.backward(40)
