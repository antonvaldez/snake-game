from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Anton's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def draw_border():
    border = Turtle()
    border.hideturtle()
    border.color("white")
    border.penup()
    border.goto(-260, 260)
    border.pendown()
    border.pensize(3)

    for _ in range(4):
        border.forward(520)
        border.right(90)

draw_border()

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        scoreboard.restart()
        snake.restart()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.restart()
            snake.restart()

screen.exitonclick()