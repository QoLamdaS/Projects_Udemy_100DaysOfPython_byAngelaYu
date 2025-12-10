import os
import sys
import random

def deal_card():
    """Random early cards generator"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def score_calculation(cards):
    """Blackjack score calculation, rules translated to Py code"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_card = {}
comp_dealer_card = {}
for i in range(2):
    user_card.append(deal_card())
    comp_dealer_card.append(deal_card())

user_score = score_calculation(user_card)
comp_dealer_score = score_calculation(comp_dealer_card)

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


elif user_wants_to_play == "no" or user_wants_to_play == "n":
    print("\nMaybe next time!\nThank you so much!\n")
    sys.exit()
else:
    print("\nCRITICAL ERROR. Invalid input. Please restart the game and type 'yes' or 'no' only please.\n")
    sys.exit()
