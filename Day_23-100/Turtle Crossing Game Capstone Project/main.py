import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
user_turtle = Player()
screen.onkey(user_turtle.move_y, "w")
cars = CarManager()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    for car in cars.all_cars:
        if car.distance(user_turtle) < 20:
            game_on = False
    if user_turtle.ycor() > 280:
        user_turtle.reset_position()
        cars.increase_speed()

print("\nGAME OVER!!!!\n")

screen.mainloop()
