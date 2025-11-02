import random
import os

os.system("cls")
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_underscores = list(chosen_word)
for i in range(len(chosen_word)):
    chosen_word_underscores[i] = "_"
print(" ".join(chosen_word_underscores))
input_guess = input("Guess a letter: ").lower()

display = []
for letter in chosen_word:
    if letter == input_guess:
        display.append(input_guess)
    else:
        display.append("_")
print(" ".join(display))