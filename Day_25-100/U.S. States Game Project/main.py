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
remaining_all_states = data.state.to_list()
score = 0

while score < 50:
    input_state = screen.textinput(title=f"{score}/{len(data.state)} U.S. States Correct", prompt="What is state's name?").title()
    if input_state in remaining_all_states:
        score += 1
        remaining_all_states.remove(input_state)
        t.goto(data.x[data.state == input_state].item(), data.y[data.state == input_state].item()) #* actually I don't know why using .item() is needed here lol 
        t.write(input_state)

screen.mainloop()