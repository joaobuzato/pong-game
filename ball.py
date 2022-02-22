from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.x_rate = 10
        self.y_rate = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_rate
        new_y = self.ycor() + self.y_rate
        self.goto(new_x, new_y)

    def bounce(self, cor='y'):
        if cor == 'y':
            self.y_rate *= -1
        elif cor == 'x':
            self.move_speed *= 0.9
            self.x_rate *= -1

    def reset_position(self):
        self.setposition(0, 0)
        self.bounce(cor='x')
        self.move_speed = 0.1

