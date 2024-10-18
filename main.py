# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 22 - Intermediate - Pong Game
# Project start day Sep-20-2024
# Going to try to code the game myself, based on steps provided by Angela

# Steps:
# 1. Create the screen - done
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

# Improvements/bugs:
# 1. Improvement: Currently, time.sleep(0.1) which adds 0.1 second delay, which is 10FPS, should be changed to ~0.03sec for 33.3FPS, however speed of ball needs to adjusted accordingly.
# 2. Improvement: In this iteration each paddle is made of multiple "turtles" and when the ball goes between the "turtles", it sinks too far into the paddle before bouncing off.
# 3. Improvement: When the ball is missed, it should probably go in the direction of the player who scored.
# 4. Improvement: In videos of pong I've seen the ball change angle after hitting a paddle depending on paddle's direction of movement?
# 5. Improvement: It would be nice if animations of ball and paddle looked smoother, as well as control.
# 6. Improvement: Increase speed after the ball hits a paddle.
# 7. Improvement: Use Stead Deck, D-pad and Y/A keys for controlling the paddles as an alternative. Use time.sleep(0.1)?

from turtle import Screen, Turtle
from paddle import Paddle, PADDLE_SIZE
from ball import Ball
from scoreboard import  Scoreboard
# from scoreboard import Scoreboard
import time

PADDLE_X_POS = 380
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINNING_SCORE = 5
X_COR_SCORE = 50
X_COR_END_GAME = 200

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")

# Create center line:
turtle_cntr_line = Turtle()
turtle_cntr_line.color("white")
turtle_cntr_line.pensize(4)
turtle_cntr_line.penup()
turtle_cntr_line.hideturtle()
turtle_cntr_line.speed("fastest")
turtle_cntr_line.goto(0, SCREEN_HEIGHT/2)
turtle_cntr_line.setheading(270)
while turtle_cntr_line.ycor() > -SCREEN_HEIGHT/2:
    turtle_cntr_line.penup()
    turtle_cntr_line.forward(15)
    turtle_cntr_line.pendown()
    turtle_cntr_line.forward(30)

screen.tracer(0) # turn off turtle animation

# Paddles creation:
paddle_left = Paddle(x_pos=-PADDLE_X_POS)
paddle_right = Paddle(x_pos=PADDLE_X_POS)

# Bind paddle control keys:
screen.listen()
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

# Ball creation:
ball = Ball()

# Score creation:
scoreboard_left = Scoreboard(-X_COR_SCORE)
scoreboard_right = Scoreboard(X_COR_SCORE)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # adds 0.1 second delay, basically sets FPS, (0.1 sec = 10FPS)
    ball.move()

    # Detect collision with top wall or bottom wall:
    if ball.ycor() > SCREEN_HEIGHT/2 - 20:
        ball.bounce_wall_top()
    elif ball.ycor() < -SCREEN_HEIGHT/2 + 20:
        ball.bounce_wall_bottom()

    # Detect collision with left or right paddle:
    for n in range(0, PADDLE_SIZE):
        if paddle_left.paddle[n].distance(ball) < 15:
            ball.bounce_left()
        elif paddle_right.paddle[n].distance(ball) < 15:
            ball.bounce_right()

    # Detect ball going out, change score, restart ball:
    if ball.xcor() > SCREEN_WIDTH/2:
        scoreboard_left.increase()
        ball.spawn()
    elif ball.xcor() < -SCREEN_WIDTH/2:
        scoreboard_right.increase()
        ball.spawn()

    # Check for winner and end game if someone won:
    if scoreboard_left.score >= WINNING_SCORE:
        scoreboard_left.game_over(text="YOU\nWON", x_cor=-X_COR_END_GAME)
        scoreboard_right.game_over(text="YOU\nLOST", x_cor=X_COR_END_GAME)
        game_is_on = False
    elif scoreboard_right.score >= WINNING_SCORE:
        scoreboard_left.game_over(text="YOU\nLOST", x_cor=-X_COR_END_GAME)
        scoreboard_right.game_over(text="YOU\nWON", x_cor=X_COR_END_GAME)
        game_is_on = False

screen.exitonclick()