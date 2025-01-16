from turtle import Turtle
import random

class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")


    def refresh(self):
        random_x = random.randint(-288, 288)
        random_y = random.randint(-288,288)
        self.goto(random_x, random_y)