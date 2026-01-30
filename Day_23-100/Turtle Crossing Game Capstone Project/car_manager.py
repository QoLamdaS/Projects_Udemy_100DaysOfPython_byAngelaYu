from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_move_distance = 5
move_increment = 10

class CarManager(Turtle):
    def __init__(self):
        '''Initializes CarManager object born with default settings.'''
        super().__init__()
        self.hideturtle() #! Hides the turtle cursor; removes it from the screen
        self.all_cars = []
        self.car_speed = starting_move_distance #* Sets the initial/default speed of the cars

    def create_car(self):
        '''Creates a new car object and appends it to the all_cars list.'''
        random_chance = random.randint(0, 5) #* Generates a random integer between 0 and 5
        if random_chance == 4: #* 1 in 6 chance to create a car; 4 is an unlucky/cursed number
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup() #! Prevents drawing lines when the cars moves
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        '''Moves all cars in the all_cars list to the left by car_speed amount.'''
        for car in self.all_cars:
            car.backward(self.car_speed) #! Moves the car backward/goto left by car_speed amount

    def increase_speed(self):
        '''Increases the speed of the cars by move_increment amount every time it is called.'''
        self.car_speed += move_increment