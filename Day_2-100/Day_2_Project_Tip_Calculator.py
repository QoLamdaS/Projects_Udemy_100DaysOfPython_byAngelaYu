
#* Project day 2 completed yeah!!

print("WELCOME di Kalkulator TIP!")
Total_Bill = float(input("What was the total bill? Rp"))
TipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
Person = int(input("How many people to split the bill? "))

EachPerson = round((Total_Bill * ((100+TipPercentage) / 100)) / Person, 2)
#Person_Rounded = round(Person_real, 2) [UNUSED]

print(f"Each person should pay: Rp{EachPerson}")