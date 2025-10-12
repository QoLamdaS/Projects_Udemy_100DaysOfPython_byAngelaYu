import os
os.system("cls")

print("Welcome to Paiton_Indonesia Pizza Deliveries!")
Pizza_Size = input("What size pizza do you want? s, m, or l: ")
Pizza_Pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
Pizza_ExtraCheese = input("Do you want extra cheese? y or n: ")

Pizza_Price = 0
if Pizza_Size == "s":
    Pizza_Price = 15
    if Pizza_Pepperoni == "y":
        Pizza_Price += 2
        if Pizza_ExtraCheese == "y":
            Pizza_Price += 1
            print(f"Your final bill is: Rp{Pizza_Price}k.")
        else:
            print(f"Your final bill is: Rp{Pizza_Price}k.")
    else:
        if Pizza_ExtraCheese == "y":
            Pizza_Price += 1
            print(f"Your final bill is: Rp{Pizza_Price}k.")
        else:
            print(f"Your final bill is: Rp{Pizza_Price}k.")
elif Pizza_Size == "m":
    Pizza_Price = 20
    if Pizza_Pepperoni == "y":
        Pizza_Price += 3
        if Pizza_ExtraCheese == "y":
            Pizza_Price += 1
            print(f"Your final bill is: Rp{Pizza_Price}k.")
        else:
            print(f"Your final bill is: Rp{Pizza_Price}k.")
    else:
        if Pizza_ExtraCheese == "y":
            Pizza_Price += 1
            print(f"Your final bill is: Rp{Pizza_Price}k.")
        else:
            print(f"Your final bill is: Rp{Pizza_Price}k.")
else:
    Pizza_Price = 25
    if Pizza_Pepperoni == "y":
        Pizza_Price += 3
        if Pizza_ExtraCheese == "y":
            Pizza_Price += 1
            print(f"Your final bill is: Rp{Pizza_Price}k.")
        else:
            print(f"Your final bill is: Rp{Pizza_Price}k.")
    else:
        if Pizza_ExtraCheese == "y":
            Pizza_Price += 1
            print(f"Your final bill is: Rp{Pizza_Price}k.")
        else:
            print(f"Your final bill is: Rp{Pizza_Price}k.")
