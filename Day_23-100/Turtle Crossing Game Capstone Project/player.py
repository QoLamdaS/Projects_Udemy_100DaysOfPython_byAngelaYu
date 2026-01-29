from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        '''Initializes player turtle object born with default settings. (sets its default attributes and methods)'''
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
    
    def move_y(self):
        move = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), move)