from turtle import Turtle, Screen
from the_snake_body import SnakeBody
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("the Snake Game VERSION!!!!!!")
screen.tracer(0)

snake = SnakeBody()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.mainloop()

