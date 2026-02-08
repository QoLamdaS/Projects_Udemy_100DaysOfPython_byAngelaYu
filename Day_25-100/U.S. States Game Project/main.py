import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game by me!!! YEAh!!")
screen.addshape("Day_25-100\\U.S. States Game Project\\blank_states_img.gif")
turtle.shape("Day_25-100\\U.S. States Game Project\\blank_states_img.gif")
t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pandas.read_csv("Day_25-100\\U.S. States Game Project\\50_states.csv")
all_us_states = data.state.to_list()

is_game_on = True
while is_game_on:
    input_state = screen.textinput(title="Guess the State???", prompt="What is state's name?").title()
    if input_state in all_us_states:
        

screen.mainloop()