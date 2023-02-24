from colorama import Fore, Style

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

game_conttinue_conditon = True

while(game_conttinue_conditon):
    direction_input = input("You are at a cross road. Where do you want to go, \"left\" or \"right\"? ")
    if direction_input == "left":
        action_input = input("You got to a lake. There is an island in the middle. Type \"wait\" to wait for a boat or type \"swim\" to cross over: ")
        if action_input == "wait":
            door_selection = input ("You arrived at the island unharmed. There is a house with 3 doors. One is Red, one is Green and the other one is Blue. Which one do you choose? ")
            if door_selection == "green":
                print(f"{Fore.GREEN}You Won!")
                print(Style.RESET_ALL)
            elif door_selection == "red" or door_selection == "blue":
                print(f"{Fore.RED}Game Over!") 
                print(Style.RESET_ALL)
        else:
            print(f"{Fore.RED}Game over!")
            print(Style.RESET_ALL)
    else:
        print(f"{Fore.RED}Game Over!") 
        print(Style.RESET_ALL)  

    game_continue = input("Do you want to go again? (yes or no) ").lower()
    if game_continue == "yes":
        print("\nHere we go again!")
        continue
    else:
        print("\nSee you again next time!")
        game_conttinue_conditon = False

