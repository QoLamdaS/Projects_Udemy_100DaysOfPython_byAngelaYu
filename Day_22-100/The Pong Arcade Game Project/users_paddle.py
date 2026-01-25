from turtle import Turtle

class LeftPaddle(Turtle):
    def __init__(self):
        '''Initializes the left paddle object born inheriting from the Turtle class and sets its defaults.'''
        super().__init__()
        self.penup()
        self.speed(0)  
        self.goto(-600, 0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def left_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def left_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class RightPaddle(Turtle):
    def __init__(self):
        '''Initializes the right paddle object born inheriting from the Turtle class and sets its defaults.'''
        super().__init__()
        self.penup()
        self.speed(0)  
        self.goto(600, 0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def right_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)
    
    def right_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)
    
    