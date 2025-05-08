from turtle import Turtle
import random

class Brick(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=2, stretch_len=3)
        self.speed("fastest")
        self.pencolor("black")
        self.pensize(2)
        self.rows = 4

    def destroy(self):
        self.hideturtle()
        self.goto(1000, 1000)
        self.clear()
        self.setheading(0)

    @staticmethod
    def create_wall(brick_colors, brick_widths, brick_height=40, rows=4):
        bricks = []
        for j in range(rows):
            x = -380
            while x < 380:
                random_width = random.choice(brick_widths)
                if x + random_width / 2 > 380:
                    break
                y = 150 - (j * brick_height)
                brick = Brick(x + random_width / 2, y, brick_colors[j])
                brick.shapesize(stretch_wid=2, stretch_len=random_width / 20)
                bricks.append(brick)
                x += random_width
        return bricks