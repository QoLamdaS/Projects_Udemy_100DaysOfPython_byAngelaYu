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

