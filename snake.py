from turtle import Turtle

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.has_turned = False

    def create_snake(self):
        for position in range(0,3):
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.goto((-20 * position), 0)
            self.snake.append(body)

    def add_segment(self, position):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.snake.append(body)

    def extend(self):
        self.add_segment(self.snake[-1].position())
    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.head.forward(20)
        self.has_turned = False

    def up(self):
        if not self.has_turned and self.head.heading() != 270:
            self.head.setheading(90)
            self.has_turned = True

    def down(self):
        if not self.has_turned and self.head.heading() != 90:
            self.head.setheading(270)
            self.has_turned = True

    def right(self):
        if not self.has_turned and self.head.heading() != 180:
            self.head.setheading(0)
            self.has_turned = True

    def left(self):
        if not self.has_turned and self.head.heading() != 0:
            self.head.setheading(180)
            self.has_turned = True

    def restart(self):
        for x in self.snake:
            x.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]