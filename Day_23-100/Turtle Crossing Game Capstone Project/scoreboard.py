from turtle import Turtle

font = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=font)

    def increase_level(self):
        self.score += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=font)
