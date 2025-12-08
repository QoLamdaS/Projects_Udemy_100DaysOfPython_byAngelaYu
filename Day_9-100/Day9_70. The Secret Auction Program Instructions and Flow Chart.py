import os

while True:
    os.system("cls")
    print("Welcome to the Silent Auction Program.")
    logo = '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
    print(logo)
    name_key = input("What is your name?: ")
    bid_value = int(input("What is your bid?: Rp"))
    bids = {}
    bids[name_key] = bid_value
    if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "no":
        os.system("cls")
        highest_bid = 0
        winner = ""
        for bidder in bids:
            bid_amount = bids[bidder] # Get the bid amount for the current bidder
            if bid_amount > highest_bid: # Check if the current bid amount is higher than the highest bid so far in dictionary
                highest_bid = bid_amount # Update the highest amount of bid so far in dictionary earlier
                winner = bidder # Update the highest bidder name so far in dictionary earlier 
        print(f"\nThe winner is {winner} with a bid of Rp{highest_bid}\n")
        break
    else:
        continue