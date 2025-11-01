import random, os

os.system("cls")
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
input_guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == input_guess:
        print("Right")
    else:
        print("Wrong")