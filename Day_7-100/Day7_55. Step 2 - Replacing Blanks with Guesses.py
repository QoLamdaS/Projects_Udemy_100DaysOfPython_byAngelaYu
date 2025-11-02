import random
import os

os.system("cls")
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
for i in range(len(chosen_word)):
    chosen_word[i] = "_"
print(" ".join(chosen_word))
input_guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == input_guess:
        print("Right")
    else:
        print("Wrong")