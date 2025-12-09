import os
import sys
import random

os.system("cls")
user_wants_to_play = input("Are you ready to play Blackjack? Type 'yes' or 'no': ").lower()
if user_wants_to_play == "yes" or user_wants_to_play == "y":
    while True:
        logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/           
"""
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

elif user_wants_to_play == "no" or user_wants_to_play == "n":
    print("\nMaybe next time!\nThank you so much!\n")
    sys.exit()
else:
    print("\nCRITICAL ERROR. Invalid input. Please restart the game and type 'yes' or 'no' only please.\n")
    sys.exit()
