from turtle import Screen
from users_paddle import LeftPaddle, RightPaddle

#! I finally taking the challenge in Lecture 160 Day 22
#! which is creating The Pong Arcade Game Project from scratch by myself without watching/peeking Dr. Angela Yu's coding/solutions.
#* Wish me luck to tackle this challenge by myself!

screen = Screen()
screen.setup(width=1.0, height=1.0) 
screen.bgcolor("black")
screen.title("The Pong Arcade Game by me!!!")

screen.listen()
user1 = LeftPaddle()
screen.onkeypress(user1.left_up, "w")
screen.onkeypress(user1.left_down, "s")
user2 = RightPaddle() #! CRUCIAL BUG: Cannot holding keypresses for left & right paddles simultaneously.
screen.onkeypress(user2.right_up, "o")
screen.onkeypress(user2.right_down, "l")

screen.mainloop()
