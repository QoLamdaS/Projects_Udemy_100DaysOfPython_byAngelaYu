from turtle import Turtle

starting_position = (0, -280)
move_distance = 10
finish_line_y = 280


class Player(Turtle):
    def __init__(self):
        '''Initializes player turtle object born with default settings. (sets its default attributes and methods)'''
        super().__init__()
        self.penup()
        self.goto(starting_position)
        self.setheading(90)
        self.shape("turtle")
    
    def move_y(self):
        move = self.ycor() + move_distance
        self.goto(self.xcor(), move)