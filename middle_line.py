from turtle import Turtle


class MiddleLine(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pensize(3)
        self.draw_line()

    def draw_line(self):
        self.goto(0, -400)
        self.setheading(90)
        for _ in range(40):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)