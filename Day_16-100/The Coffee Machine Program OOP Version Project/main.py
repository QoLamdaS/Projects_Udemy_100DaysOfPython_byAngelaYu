import os
import sys

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to the 'VIRTUAL' Coffee Machine Program! OOP VERSION!!!!\n")
main_menu = Menu()
main_coffee_maker = CoffeeMaker()
main_money_machine = MoneyMachine()

while True:
    user_wants = input("What would you like? (espresso/latte/cappuccino) or maybe 'off' and 'report': ").lower()
    if user_wants == "off":
        print("\nTurning off the coffee machine. Goodbye!\n")
        sys.exit()
    elif user_wants == "report":
        main_coffee_maker.report()
        main_money_machine.report()
    else:
        the_drink = main_menu.find_drink(user_wants)
        if main_coffee_maker.is_resource_sufficient(the_drink):
            if main_money_machine.make_payment(the_drink.cost):
                main_coffee_maker.make_coffee(the_drink)
