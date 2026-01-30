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
screen.onkeypress(user_turtle.move_y, "w")
cars = CarManager()
level = Scoreboard()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    for car in cars.all_cars: #* Checks for collision between each car in all_cars list and the user_turtle current position
        if car.distance(user_turtle) < 20:
            level.game_over()
            game_on = False
    if user_turtle.ycor() > 280: #* Checks if the user_turtle has reached the top of the screen and increases the level + cars' speed
        user_turtle.reset_position()
        level.increase_level()
        cars.increase_speed()

screen.mainloop()
