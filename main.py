import time
import pygame
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard

MAX_MISSED_BALLS = 3

divider = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -270))
ball = Ball()
scoreboard = Scoreboard()

brick_colors = ["red", "orange", "yellow", "green"]
brick_widths = [40, 60, 80]
bricks = Brick.create_wall(brick_colors, brick_widths)

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

# Load sound effects
pygame.mixer.init()
paddle_hit = pygame.mixer.Sound("./sound_effects/paddle_hit.wav")
wall_hit = pygame.mixer.Sound("./sound_effects/wall_hit.wav")
rock_hit = pygame.mixer.Sound("./sound_effects/rock_hit.mp3")
speed_up = pygame.mixer.Sound("./sound_effects/speed_up.mp3")
level_up = pygame.mixer.Sound("./sound_effects/level_up.mp3")
lose_point = pygame.mixer.Sound("./sound_effects/lose_point.wav")
game_over = pygame.mixer.Sound("./sound_effects/game_over.wav")

game_is_on = True
brick_hit_count = 0
speed_increased = False
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()
        wall_hit.play()

    # Detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce_y()
        wall_hit.play()

    # Detect collision with paddle
    if ball.distance(paddle) < 100 and ball.ycor() < -240:
        ball.bounce_y()
        paddle_hit.play()

    # Detect collision with bricks
    for brick in [obj for obj in screen.turtles() if isinstance(obj, Brick)]:
        brick_width = brick.shapesize()[1] * 20
        brick_height = brick.shapesize()[0] * 20

        if (
            brick.xcor() - brick_width / 2 - 11
            < ball.xcor()
            < brick.xcor() + brick_width / 2 + 11
            and brick.ycor() - brick_height / 2 - 11
            < ball.ycor()
            < brick.ycor() + brick_height / 2 + 11
        ):
            x_diff = abs(ball.xcor() - brick.xcor())
            y_diff = abs(ball.ycor() - brick.ycor())

            if y_diff > x_diff:
                ball.bounce_y()
            else:
                ball.bounce_x()

            brick.destroy()
            rock_hit.play()
            brick_hit_count += 1
            if brick_hit_count >= 5 and not speed_increased:
                speed_up.play()
                ball.move_speed *= 0.70
                speed_increased = True

    # Detect paddle missed
    if ball.ycor() < -280:
        ball.reset_position(paddle_position=(paddle.xcor(), -240))
        scoreboard.misses()
        lose_point.play()
        time.sleep(0.5)
        brick_hit_count = 0
        speed_increased = False

    # Level Up
    if all(brick.isvisible() is False for brick in bricks):
        ball.reset_position(paddle_position=(paddle.xcor(), -240))
        brick_hit_count = 0
        scoreboard.miss = 0
        speed_increased = False
        scoreboard.level_up()
        ball.lv_up()
        ball.move_speed = ball.current_lv_speed
        level_up.play()
        if scoreboard.current_lv >= 4:
            brick_colors = ["darkred", "darkblue", "darkgreen", "gray", "gold"]
            bricks = Brick.create_wall(brick_colors, brick_widths, rows=5)
        elif scoreboard.current_lv % 2 == 0:
            brick_colors = ["blue", "purple", "pink", "cyan"]
            bricks = Brick.create_wall(brick_colors, brick_widths)
        else:
            brick_colors = ["red", "orange", "yellow", "green"]
            bricks = Brick.create_wall(brick_colors, brick_widths)
        time.sleep(0.5)

    if scoreboard.miss == MAX_MISSED_BALLS:
        game_is_on = False
        game_over.play()
        scoreboard.game_over()
        ball.hideturtle()


screen.exitonclick()
