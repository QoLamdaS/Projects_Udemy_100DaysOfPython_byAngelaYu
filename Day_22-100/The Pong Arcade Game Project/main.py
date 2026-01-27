from turtle import Screen
from users_paddle import LeftPaddle, RightPaddle
from the_ball import Ball
import time

#! UPDATE: I "give up" taking the challenge "The Pong Arcade Game Project" without watching Dr. Angela's codings/solutions.
#* It is time-consuming (multiple days to complete) and I have other priorities to focus on such as school assignments and upcoming exams.
#* However at least I have tried to create a novel project on my own. So it is not a total loss I think.
#* I finally decided to follow Dr. Angela's recommendation to watch her codings (Lecture 160 Day 22)

screen = Screen()
screen.setup(width=800, height=600) 
screen.bgcolor("black")
screen.title("The Pong Arcade Game by me!!!")
screen.tracer(0)

screen.listen()
user1 = LeftPaddle()
screen.onkey(user1.left_up, "w")
screen.onkey(user1.left_down, "s")
user2 = RightPaddle()
screen.onkey(user2.right_up, "o")
screen.onkey(user2.right_down, "l")
ball = Ball()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        #* Detect collision with up & down wall; and then bounce the ball (reverse its y direction).
        ball.bounce_y()
    if ball.distance(user2) < 50 and ball.xcor() > 320 or ball.distance(user1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > -380:
        #* Detect when Left paddle misses the ball.
        ball.reset_position()
    if ball.xcor() < 380:
        #* Detect when Right paddle misses the ball.
        ball.reset_position()

screen.mainloop()
