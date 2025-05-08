from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.current_lv = 1
        self.miss = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.goto(280, 230)
        self.write(f"Level: {self.current_lv}", align="center", font=("Courier", 30, "normal"))
        if self.miss < 1:
            self.color("green")
        elif self.miss < 2:
            self.color("yellow")
        elif self.miss < 3:
            self.color("orange")
        else:
            self.color("red")
        self.goto(-280, 230)
        self.write(f"Miss: {self.miss}", align="center", font=("Courier", 30, "normal"))

    def level_up(self):
        self.current_lv += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -50)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))

    def misses(self):
        self.miss += 1
        self.update_scoreboard()
