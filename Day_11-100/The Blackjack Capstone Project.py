import os
import sys

os.system("cls")
user_wants_to_play = input("Are you ready to play Blackjack? Type 'yes' or 'no': ").lower()
if user_wants_to_play == "yes" or user_wants_to_play == "y":
    print("testing only")
elif user_wants_to_play == "no" or user_wants_to_play == "n":
    print("\nMaybe next time!\nThank you so much!\n")
    sys.exit()
else:
    print("CRITICAL ERROR. Invalid input. Please restart the game and type 'yes' or 'no' only please.")
    sys.exit()
