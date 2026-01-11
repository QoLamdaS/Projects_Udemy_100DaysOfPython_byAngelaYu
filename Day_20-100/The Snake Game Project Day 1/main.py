from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("the Snake Game VERSION!!!!!!")
screen.tracer(0)

all_blocks = []
for i in range(3):
    new_block = Turtle(shape="square")
    new_block.color("white")
    new_block.penup()
    new_block.goto(x=0 - 20 * i, y=0)
    all_blocks.append(new_block)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for block_num in range(len(all_blocks) - 1, 0, -1):
        new_x = all_blocks[block_num - 1].xcor()
        new_y = all_blocks[block_num - 1].ycor()
        all_blocks[block_num].goto(x=new_x, y=new_y)
    all_blocks[0].forward(20)

screen.mainloop()
