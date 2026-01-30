from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_move_distance = 5
move_increment = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = starting_move_distance

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 4:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += move_increment