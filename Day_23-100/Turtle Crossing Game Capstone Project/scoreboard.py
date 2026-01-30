from turtle import Turtle

font = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        '''Initializes Scoreboard object born with default settings.'''
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_level()

    def update_level(self):
        '''Clears and then updates the level display on the screen.'''
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=font)

    def increase_level(self):
        '''Increases the level by 1 and then updates the level display on the screen.'''
        self.score += 1
        self.update_level()

    def game_over(self):
        '''Displays "GAME OVER!!!" on the screen.'''
        self.goto(0, 0)
        self.write("GAME OVER!!!", align="center", font=font)
