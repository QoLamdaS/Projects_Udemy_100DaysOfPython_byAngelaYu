import os
os.system("cls")

print('''

                    _,__        .:
            Darwin <*  /        | \
               .-./     |.     :  :,
              /           '-._/     \_
             /                '       \
           .'                         *: Brisbane
        .-'                             ;
        |                               |
        \                              /
         |                            /
   Perth  \*        __.--._          /
           \     _.'       \:.       |
           >__,-'             \_/*_.-'
                                 Melbourne
        snd                     :--,
                                 '/


      ''')

print("\nWelcome to Treasure Island. Australian Version???\nYour mission is to find the Silver CHEST.")

Left_or_Right = input("You're at a crossroad. Where do you want to go?\nType 'left' or 'right': ")
if Left_or_Right.lower() == "left":
    Wait_or_Swim = input("You come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across: ")
    if Wait_or_Swim.lower() == "wait":
        Door_RedYellowBlue = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which color do you choose?: ")
        if Door_RedYellowBlue.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif Door_RedYellowBlue.lower() == "yellow":
            print("You found the Silver_CHEST! You Win!")
        else:
            print("DEATH. Game Over.")
    else:
        print("DEATH. Game Over.")
else:
    print("DEATH. Game Over.")


