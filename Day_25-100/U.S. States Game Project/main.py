import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game by me!!! YEAh!!")
screen.addshape("Day_25-100\\U.S. States Game Project\\blank_states_img.gif")
turtle.shape("Day_25-100\\U.S. States Game Project\\blank_states_img.gif")

input_state = screen.textinput(title="Guess the State???", prompt="What is state's name?").title()
print(input_state)

screen.mainloop()