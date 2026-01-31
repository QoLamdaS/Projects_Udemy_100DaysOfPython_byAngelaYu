from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("D:\downloadrandom\Projects_Udemy_100DaysOfPython_byAngelaYu\Day_24-100\The Snake Game from Dr.Yu\the_data.txt", mode="r+") as data_score:
            self.high_score = int(data_score.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scores(self):
        if self.score > self.high_score: #* Check if current score is greater than the high score
            self.high_score = self.score
            with open("the_data.txt", mode="w") as data_score:
                data_score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
