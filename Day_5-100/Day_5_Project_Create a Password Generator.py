import string
import random
import os
os.system("cls")

print("Welcome to the Py_Password Generator my VERSION!")
NumLetters = int(input("How many letters would you like in your password? "))
NumSymbols = int(input("How many symbols would you like in your password? "))
NumDigits = int(input("How many digits would you like in your password? "))

all_digitsWhole = list(string.digits)
all_symbols = list(string.punctuation)
all_letters = list(string.ascii_letters)
password = []
for i in range(NumLetters):
    password.append(random.choice(all_letters))
for i in range(NumSymbols):
    password.append(random.choice(all_symbols))
for i in range(NumDigits):
    password.append(random.choice(all_digitsWhole))

random.shuffle(password)
password = "".join(password)
print(f"Your new generated password is: {password}")