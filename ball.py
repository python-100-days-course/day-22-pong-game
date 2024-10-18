# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 22 - Intermediate - Pong Game
# Project start day Sep-20-2024

# Improvements/bugs:
# 1. Bounce methods should be simplified and made to work with any angle.
# 2. Possibly make ball starting position and angles more random?


from turtle import Turtle
import random

TURTLE_SIZE = 20
STARTING_POS = (0, 0)
STARTING_DIRECTIONS = [45, 135, 225, 315] # 45 deg in 4x directions
MOVE_DISTANCE = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.spawn()

    def spawn(self):
        self.goto(STARTING_POS)
        self.setheading(random.choice(STARTING_DIRECTIONS))
        self.tiltangle(45) # keeps the square facing in same direction, depends on starting angle, currently only works with 45deg increment angles

    def move(self):
        self.forward(MOVE_DISTANCE)

    # Assuming fully elastic collision and 45 deg angles.
    # 45 -> 315
    # 135 -> 225
    # 225 -> 135
    # 315 -> 45
    def bounce_wall_top(self): # should work with any initial angle
        initial_heading = self.heading()
        # print(f"initial_heading = {initial_heading}")
        if 0 < initial_heading < 90: # 45 (0-90)
            new_heading = 360 - initial_heading # 315
            # print(f"new_heading = {new_heading}")
            self.setheading(new_heading)
        elif 90 < initial_heading < 180: # 135 (90-180)
            new_heading = 270 - (initial_heading - 90) # 225
            # print(f"new_heading = {new_heading}")
            self.setheading(new_heading)

    def bounce_wall_bottom(self): # currently only works with 225 and 315 initial angles, need to modify
        initial_heading = self.heading()
        if initial_heading == 225:
            self.setheading(135)
        elif initial_heading == 315:
            self.setheading(45)

    def bounce_left(self):
        initial_heading = self.heading()
        if initial_heading == 225:
            self.setheading(315)
        elif initial_heading == 135:
            self.setheading(45)

    def bounce_right(self):
        initial_heading = self.heading()
        if initial_heading == 45:
            self.setheading(135)
        elif initial_heading == 315:
            self.setheading(225)
