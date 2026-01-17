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
        #* Detect collision with food; a.k.a detect Snake eating the random spawned food and then grow 'get longer'.
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -285 or snake.segments[0].ycor() > 285 or snake.segments[0].ycor() < -285:
        #* Detect collision with wall; a.k.a detect Snake hitting the maximum wall from player view
        game_is_on = False

    for segment in snake.segments:
        #* Detect collision with tail; a.k.a detect Snake hitting its own body
        if segment == snake.segments[0]: #! The very first segment is the Snake's head. So this condition is to skip the head.
            continue
        elif snake.segments[0].distance(segment) < 10:
            game_is_on = False

score.game_over()

screen.mainloop()

