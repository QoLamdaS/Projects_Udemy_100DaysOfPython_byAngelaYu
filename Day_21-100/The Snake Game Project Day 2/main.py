from turtle import Screen
from the_snake_body import SnakeBody
from the_food import FoodSnake
from scoreboard_file import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("the Snake Game VERSION!!!!!!")
screen.tracer(0)

snake = SnakeBody()
food = FoodSnake() 
score = ScoreBoard()

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
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -285 or snake.segments[0].ycor() > 285 or snake.segments[0].ycor() < -285:
        game_is_on = False
    

score.game_over()

screen.mainloop()

