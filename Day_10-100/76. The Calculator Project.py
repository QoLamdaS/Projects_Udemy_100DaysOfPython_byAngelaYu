import os

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

mathematical_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#print(mathematical_operations["*"](n1=4, n2=8))
while True:
    os.system("cls")
    logo = '''
 _____________________
|  _________________  |
| |              /  | |
| |       /\    /   | |
| |  /\  /  \  /    | |
| | /  \/    \/     | |
| |/             JO | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

    '''
    print(logo)
    user_num1 = float(input("What is your the first number?: "))
    while True:
        for symbol in mathematical_operations:
            print(symbol)
        user_symbol = input("Pick an operation from the line above to calculate: ")
        user_next_num = float(input("What is your the next number?: "))
        
        calculated_result = mathematical_operations[user_symbol](n1=user_num1, n2=user_next_num)
        
        print(f"{user_num1} {user_symbol} {user_next_num} = {calculated_result}")
        if input(f"Type 'yes' to continue calculating with {calculated_result}, or type 'no' to start a new calculation.: ").lower() == 'yes':
            user_num1 = calculated_result
            continue
        else:
            break
