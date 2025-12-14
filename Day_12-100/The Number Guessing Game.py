import logo_TheNumberGuessingGame
import os
import random
import sys

def generate_answer():
    """Generates a random number between 1 and 100 every-time you call it, IT ISN'T FIXED, so each time you call it, it will return a different number."""
    return random.randint(1, 100)
fixed_answer = generate_answer()

os.system('cls' if os.name == 'nt' else 'clear')
print(logo_TheNumberGuessingGame.the_logo)
print("Welcome to The Number Guessing Game! YEAH!!!!!!")

if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "hard":
    for attempt in range(5, 0, -1):
        print(f"You have {attempt} attempts remaining to guess the number.\n")
        guess = int(input("Make a guess: "))
        if guess > fixed_answer:
            print("Too high.")
        elif guess < fixed_answer:
            print("Too low.")
        else:
            print(f"\nYou got it! The answer was {fixed_answer}.\n")
            sys.exit()
    print("You lose. TRY AGAIN!!!!!!!!!!")
    sys.exit()
else:
    for attempt in range(10, 0, -1):
        print(f"You have {attempt} attempts remaining to guess the number.\n")
        guess = int(input("Make a guess: "))
        if guess > fixed_answer:
            print("Too high.")
        elif guess < fixed_answer:
            print("Too low.")
        else:
            print(f"\nYou got it! The answer was {fixed_answer}.\n")
            sys.exit()
    print("DEFEATED!!")
    sys.exit()