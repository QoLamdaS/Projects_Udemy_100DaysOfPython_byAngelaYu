from turtle import Screen
from user1_paddle import LeftPaddle

#! I finally taking the challenge in Lecture 160 Day 22
#! which is creating The Pong Arcade Game Project from scratch by myself without watching/peeking Dr. Angela Yu's coding/solutions.
#* Wish me luck to tackle this challenge by myself!

screen = Screen()
screen.setup(width=1.0, height=1.0) 
screen.bgcolor("black")
screen.title("The Pong Arcade Game by me!!!")

user1 = LeftPaddle()

screen.listen()
screen.onkey(user1.left_up, "w")
screen.onkey(user1.left_down, "s")


screen.mainloop()
