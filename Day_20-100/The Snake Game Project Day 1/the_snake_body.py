from turtle import Turtle

class SnakeBody:
    #! ERROR ERROR ERROR ERROR
    def __init__(self, all_blocks, screen):
        game_is_on = True
        while game_is_on:
            screen.update()
            time.sleep(0.1)
            for block_num in range(len(all_blocks) - 1, 0, -1):
                new_x = all_blocks[block_num - 1].xcor()
                new_y = all_blocks[block_num - 1].ycor()
                all_blocks[block_num].goto(x=new_x, y=new_y)
            all_blocks[0].forward(20)
    