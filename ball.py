from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, -240)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.current_lv_speed = .1
        self.move_speed = self.current_lv_speed
        self.setheading(0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
        # self.move_speed *= 0.9

    def reset_position(self, paddle_position):
        self.goto(paddle_position)
        self.move_speed = self.current_lv_speed
        self.bounce_y()
        self.setheading(0)

    def lv_up(self):
        self.current_lv_speed = max(self.current_lv_speed * 0.85, 0.01)

