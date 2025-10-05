print("WELCOME di Kalkulator TIP!")
Total_Bill = float(input("What was the total bill? Rp"))
TipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
Person = int(input("How many people to split the bill? "))

Person_real = (Total_Bill + (TipPercentage / 100)) / Person
Person_Rounded = round(Person_real, 2)

print(f"Each person should pay: Rp{Person_Rounded}")