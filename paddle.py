# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 22 - Intermediate - Pong Game
# Project start day Sep-20-2024

# Improvements/bugs:
# 1. Should a single turtle per paddle by stretching it with .shapesize(strech_wid=x, sretch_lin=1), improvement. Slightly complicates collision with the ball.
# 2. Paddle object should inherit from Turtle class, e.g. class Paddle(Turtle)....

from turtle import Turtle

# Reference code from snake game
SCREEN_WIDTH_P = 800
SCREEN_HEIGHT_P = 600
PADDLE_SIZE = 5 # num of squares (turtles)
TURTLE_SIZE = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:
    def __init__(self, x_pos):
        self.paddle = []
        self.segments_coordinates = []
        for n in range(0,PADDLE_SIZE):
            y_pos = (PADDLE_SIZE * TURTLE_SIZE) / 2 - n * TURTLE_SIZE
            new_coordinate = (x_pos, y_pos)
            self.segments_coordinates.append(new_coordinate)
        print(self.segments_coordinates)
        for position in self.segments_coordinates:
            # self.segments[-1].position()
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.speed("fastest")
            new_segment.penup()
            new_segment.goto(position)
            self.paddle.append(new_segment)

    def up(self):
        if self.paddle[0].ycor() < SCREEN_HEIGHT_P/2 - TURTLE_SIZE/2:
            for seg_num in range(0, len(self.paddle)):
                self.paddle[seg_num].setheading(UP)
                self.paddle[seg_num].forward(MOVE_DISTANCE)

    def down(self):
        if self.paddle[-1].ycor() > -(SCREEN_HEIGHT_P / 2 - TURTLE_SIZE / 2):
            for seg_num in range(0, len(self.paddle)):
                self.paddle[seg_num].setheading(DOWN)
                self.paddle[seg_num].forward(MOVE_DISTANCE)