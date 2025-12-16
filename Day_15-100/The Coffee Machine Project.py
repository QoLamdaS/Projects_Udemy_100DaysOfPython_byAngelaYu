import os
import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def ingredients_sufficiency(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient to make 
    before running process_coins() function."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coins():
    """To know total coins inserted by the user and then converted to Dollars."""
    print("Please insert coins.")
    user_coins = int(input("How many quarters?: ")) * 0.25
    user_coins += int(input("How many dimes?: ")) * 0.10
    user_coins += int(input("How many nickels?: ")) * 0.05
    user_coins += int(input("How many pennies?: ")) * 0.01
    return user_coins


os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to the 'VIRTUAL' Coffee Machine Program!\n")

while True:
    user_wants = input("What would you like? (espresso/latte/cappuccino) or maybe 'off' and 'report': ").lower()
    if 
    
    else:
        print("\nTurning off the coffee machine. Goodbye!\n")
        sys.exit()

