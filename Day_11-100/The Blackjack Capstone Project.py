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

def compare(user_score, comp_dealer_score):
    """Compare user and computer dealer scores and declare the winner"""
    if user_score == comp_dealer_score:
        return "It's a Draw!"
    elif comp_dealer_score == 0:
        return "You Lose! Computer dealer has a Blackjack!"
    elif user_score == 0:
        return "You Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You Lose!"
    elif comp_dealer_score > 21:
        return "Computer dealer went over. You Win!"
    elif user_score > comp_dealer_score:
        return "YOU WIN!!!"
    else:
        return "YOU LOSE!!!"

# user_card = []
# comp_dealer_card = []
# for i in range(2):
#     user_card.append(deal_card())
#     comp_dealer_card.append(deal_card())

# user_score = score_calculation(user_card)
# comp_dealer_score = score_calculation(comp_dealer_card)

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
        
        user_card = []
        comp_dealer_card = []
        for i in range(2):
            user_card.append(deal_card())
            comp_dealer_card.append(deal_card())
        user_score = score_calculation(user_card)
        comp_dealer_score = score_calculation(comp_dealer_card)

        while True:
            print(f"Your cards: {user_card} ; and your current score: {user_score}") # To show all the cards and first score of the user from player POV
            print(f"Computer dealer's first card: {comp_dealer_card[0]}") # To show only the first card of the computer_dealer from player POV
            user_choice = input("Type 'hit' to get another card, type 'pass' to pass: ").lower()
            if user_choice == "hit":
                user_card.append(deal_card())
            else:
                break
        user_score = score_calculation(user_card)
        while comp_dealer_score < 17:
            comp_dealer_card.append(deal_card())
            comp_dealer_score = score_calculation(comp_dealer_card)

        print(f"Your final hand: {user_card} ; and your final score: {user_score}")
        print(f"Computer dealer's final hand: {comp_dealer_card} ; and computer dealer's final score: {comp_dealer_score}")
        print(compare(user_score, comp_dealer_score))
        play_again = input("\nDo you want to play a new game of Blackjack? Type 'yes' or 'no': ").lower()
        if play_again == "yes" or play_again == "y":
            os.system("cls")
            continue
        else:
            print("\nThank you so much for playing! Goodbye!\n")
            sys.exit()

elif user_wants_to_play == "no" or user_wants_to_play == "n":
    print("\nMaybe next time!\nThank you so much!\n")
    sys.exit()
else:
    print("\nCRITICAL ERROR. Invalid input. Please restart the game and type 'yes' or 'no' only please.\n")
    sys.exit()
