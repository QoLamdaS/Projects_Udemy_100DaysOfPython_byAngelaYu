import os
import random
from art_ownascii import logo, vs
from data_forgame import data

os.system('cls' if os.name == 'nt' else 'clear')
print(logo)

score = 0
while True:
    option_a = random.choice(data)
    option_b = random.choice(data)
    if option_a == option_b:
        option_b = random.choice(data)
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if option_a['follower_count'] > option_b['follower_count']:
        correct_answer = "A"
    else:
        correct_answer = "B"
    if user_guess == correct_answer:
        score += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"CORRECT! You're current score is: {score}.\n")
        continue
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"WRONG!!!!Game Over. Your final score is: {score}.\n")
        break