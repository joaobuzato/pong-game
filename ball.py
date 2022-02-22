from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.x_rate = 10
        self.y_rate = 10

    def move(self):
        new_x = self.xcor() + self.x_rate
        new_y = self.ycor() + self.y_rate
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_rate *= -1

    def bounce_back(self):
        self.x_rate *= -1