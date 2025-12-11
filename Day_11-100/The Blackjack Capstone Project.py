import os
import sys
import random

Blackjack_logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/           
"""

def deal_card():
    """Random early cards generator"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def score_calculation(cards):
    """Blackjack score calculation, rules translated to Py code"""
    if sum(cards) == 21 and len(cards) == 2: # Check for a blackjack
        return 0
    if 11 in cards and sum(cards) > 21: # Convert Aces (11 → 1) if needed
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

def clear():
    """Function to clear the console screen cross-platform"""
    os.system("cls" if os.name == "nt" else "clear")

clear()
User_wants_to_play = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
if User_wants_to_play == "no" or User_wants_to_play == "n":
    print("\nMaybe next time!\nThank you so much! =)\n")
    sys.exit()

while True:
    clear()
    print(Blackjack_logo)
    # Dealing initial cards for player and computer dealer for two lines below
    user_cards = [deal_card(), deal_card()]
    comp_dealer_cards = [deal_card(), deal_card()]

    user_score = score_calculation(user_cards)
    comp_dealer_score = score_calculation(comp_dealer_cards)

    print(f"Your cards: {user_cards} ; and your current score: {user_score}")
    print(f"Computer dealer's first card: {comp_dealer_cards[0]}")

    if user_score == 0 or comp_dealer_score == 0: # Check for instant blackjack
        print(compare(user_score, comp_dealer_score))
        play_again = input("\nPlay a game of Blackjack again? Type 'yes' or 'no': ").lower()
        if play_again == "no" or play_again == "n":
            print("\nThank you so much for playing! =)\n")
            sys.exit()
        else:
            continue
    
    while user_score != 0 and user_score < 21: # Player's turn for hit or stand
        user_choice = input("Type 'hit' to get another card, or type 'stand' to pass: ").lower()
        if user_choice == "hit":
            user_cards.append(deal_card())
            user_score = score_calculation(user_cards)
            print(f"\nYour cards: {user_cards} ; and your current score: {user_score}")
            print(f"Computer dealer's first card: {comp_dealer_cards[0]}")
            if user_score > 21:
                break
        else:
            break
    
    while comp_dealer_score != 0 and comp_dealer_score < 17: # Computer dealer's turn to draw cards
        comp_dealer_cards.append(deal_card())
        comp_dealer_score = score_calculation(comp_dealer_cards)

    print("\nFINAL RESULTS:\n")
    print(f"Your final hand: {user_cards} ; and your final score: {user_score}")
    print(f"Computer dealer's final hand: {comp_dealer_cards} ; and computer dealer's final score: {comp_dealer_score}")
    print(compare(user_score, comp_dealer_score))
    play_again = input("\nPlay a game of Blackjack again? Type 'yes' or 'no': ").lower()
    if play_again == "no" or play_again == "n":
        print("\nThank you so much for playing! =)\n")
        sys.exit()
    else:
        continue



