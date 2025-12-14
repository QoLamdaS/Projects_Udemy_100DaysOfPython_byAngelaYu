import logo_TheNumberGuessingGame
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')
print(logo_TheNumberGuessingGame.the_logo)

def the_answer():
    return random.randint(1, 100)


