import random
import os

os.system("cls")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Rock Paper Scissor")
Player_Input = input("Rock, Paper, or Scissor? ").upper()
Computer_Input = random.choice(["rock", "paper", "scissor"])

if Player_Input == "ROCK" and Computer_Input == "rock":
    print(f"You: \n{rock}\nComputer:\n {rock}")
    print("Draw!!!")
elif Player_Input == "ROCK" and Computer_Input == "paper":
    print(f"You: \n{rock}\nComputer:\n {paper}")
    print("You Lose!!!")
elif Player_Input == "ROCK" and Computer_Input == "scissor":
    print(f"You: \n{rock}\nComputer:\n {scissors}")
    print("You Win!!!")

if Player_Input == "PAPER" and Computer_Input == "paper":
    print(f"You: \n{paper}\nComputer:\n {paper}")
    print("Draw!!!")
elif Player_Input == "PAPER" and Computer_Input == "rock":
    print(f"You: \n{paper}\nComputer:\n {rock}")
    print("You Win!!!")
elif Player_Input == "PAPER" and Computer_Input == "scissor":
    print(f"You: \n{paper}\nComputer:\n {scissors}")
    print("You Lose!!!")

if Player_Input == "SCISSOR" and Computer_Input == "scissor":
    print(f"You: \n{scissors}\nComputer:\n {scissors}")
    print("Draw!!!")
elif Player_Input == "SCISSOR" and Computer_Input == "rock":
    print(f"You: \n{scissors}\nComputer:\n {rock}")
    print("You Lose!!!")
elif Player_Input == "SCISSOR" and Computer_Input == "paper":
    print(f"You: \n{scissors}\nComputer:\n {paper}")
    print("You Win!!!")

