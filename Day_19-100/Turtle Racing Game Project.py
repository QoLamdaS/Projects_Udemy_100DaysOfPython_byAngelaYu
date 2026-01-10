from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-70 + i*30)
    all_turtles.append(new_turtle)

race_on = False
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"\nYou've won! The {winning_color} turtle is the winner!\n")
            else:
                print(f"\nYou've lost! The {winning_color} turtle is the winner!\n")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

