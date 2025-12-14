import logo_TheNumberGuessingGame
import os
import random

def the_answer():
    return random.randint(1, 100)

os.system('cls' if os.name == 'nt' else 'clear')
print(logo_TheNumberGuessingGame.the_logo)
print("Welcome to The Number Guessing Game! YEAH!!!!!!")

if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "hard":
    print("difficult")
else:
    print("easy")

