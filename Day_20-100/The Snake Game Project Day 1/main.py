from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("the Snake Game VERSION!!!!!!")

all_blocks = []
for i in range(3):
    new_block = Turtle(shape="square")
    new_block.color("white")
    new_block.goto(x=0 - 20 * i, y=0)
    all_blocks.append(new_block)

screen.mainloop()
