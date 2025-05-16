from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("green")
        self.speed("fastest")
        self.goto((random.randint(-240 // 20, 240 // 20)) * 20, (random.randint(-240 // 20, 240 // 20) * 20))
        self.refresh()

    def refresh(self):
        colors = ["green", "red", "blue", "yellow"]
        self.color(random.choice(colors))
        self.goto((random.randint(-240 // 20, 240 // 20)) * 20, (random.randint(-240 // 20, 240 // 20) * 20))