import random
import os

hangman_pics = [
    """
   +---+
   |   |
       |
       |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
       |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
    """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
========="""
]

os.system("cls")
print(hangman_pics[0])
print("\nWelcome to Hangman Game!\n")

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print (placeholder)

correct_letters = []
player_lives = 6

while True:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    if guess not in chosen_word:
        player_lives -= 1
        if player_lives == 0:
            os.system("cls")
            print(hangman_pics[6])
            print("\nYou lose!!!!!!!!!!!!\n")
            break
        else:
            print(hangman_pics[6 - player_lives])
            print(f"You have {player_lives} / 6 lives left")

    if "_" not in display:
        os.system("cls")
        print("\nYEAH, You win!!!!!!!!!!!!\n")
        break