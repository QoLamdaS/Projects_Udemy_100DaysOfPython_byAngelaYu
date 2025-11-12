import random
import os

os.system("cls")
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print (placeholder)

correct_letters = []

while True:
    guess = input("Guess a letter: ").lower()
    player_lives = 6
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

    if "_" not in display:
        os.system("cls")
        break

print("\nYEAH, You win!!!!!!!!!!!!\n")