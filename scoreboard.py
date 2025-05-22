from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("courier",24,"normal"))
        self.hideturtle()

    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("courier", 24, "normal"))

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open ("high_score.txt", mode="w") as file:
                    file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("courier", 24, "normal"))