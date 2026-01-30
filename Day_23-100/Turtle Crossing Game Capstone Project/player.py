from turtle import Turtle

starting_position = (0, -280)
move_distance = 10

class Player(Turtle):
    def __init__(self):
        '''Initializes player turtle object born with default settings. (sets its default attributes and methods)'''
        super().__init__()
        self.penup()
        self.goto(starting_position)
        self.setheading(90)
        self.shape("turtle")

    def move_y(self):
        '''Moves the player turtle object upward_y by move_distance amount.'''
        move = self.ycor() + move_distance
        self.goto(self.xcor(), move)

    def reset_position(self):
        '''Resets the player turtle object position to the default starting position.'''
        self.goto(starting_position)