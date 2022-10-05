from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.goto((0, 0))
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .1

    def move(self):
        new_pos_y = self.ycor() + self.y_move
        new_pos_x = self.xcor() + self.x_move
        self.goto((new_pos_x, new_pos_y))

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
        self.move_speed = .1

    def increase_speed(self):
        self.move_speed /= 1.5

