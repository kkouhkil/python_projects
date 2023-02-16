import random as r
from colorama import Fore, Style

# Getting player choice
def get_player_choice():
    player_choise_satisfaction = True

    while(player_choise_satisfaction):
        player_choice = input("\nEnter your choice please (Rock, Paper, Scissors): ")
        player_choice_tmp = player_choice.lower()

        if player_choice_tmp == "rock" or player_choice_tmp == "paper" or player_choice_tmp == "scissors":
            player_choise_satisfaction = False

        else:
            print("WRONG INPUT! Select only one choice from Rock, Paper and Scissors!")
            player_choise_satisfaction = True

    player_choice_first_letter = player_choice[0].upper()
    player_choice = player_choice_first_letter + player_choice_tmp[1:]

    return player_choice

# Getting computer choice
def get_computer_choice():
    computer_choice_list = ["Rock", "Paper", "Scissors"]
    computer_choice = r.choice(computer_choice_list)

    return computer_choice

# Defining the game rule
def game_rule(player_choice,computer_choice):

    if player_choice == "Rock":
        if computer_choice == "Paper":
            game_result = Fore.RED + "You Lost!, Try again!" 

        if computer_choice == "Scissors":
            game_result = Fore.GREEN + "Congratulaitons, You Won!"
    
    if player_choice == "Paper":
        if computer_choice == "Rock":
            game_result = Fore.GREEN + "Congratulaitons, You Won!"

        if computer_choice == "Scissors":
            game_result = Fore.RED + "You Lost!, Try again!"   

    if player_choice == "Scissors":
        if computer_choice == "Paper":
            game_result = Fore.GREEN + "Congratulaitons, You Won!"

        if computer_choice == "Rock":
            game_result = Fore.RED + "You Lost!, Try again!"
       
    if player_choice == computer_choice:
        game_result = Fore.BLUE + "It's a Draw!, No one is the winner!"   
 
    return game_result
    
# Greeting the user and asking for his/her name    
def greeting (name):
    greeting_message = "\nHi " + Fore.CYAN + name + Style.RESET_ALL + ", Welcome to the Rock-Paper-Scissors game!"
    print(greeting_message)
    return greeting_message

# Defining the Rock-Paper-Scissors game function
def rock_paper_scissors_game():
    name = input("\nEnter your name please: ")
    greeting(name)

    while(True):
        print(Style.RESET_ALL) 
        
        player_choice_call = get_player_choice()
        print("\nYou chose:", player_choice_call)
        computer_choice_call = get_computer_choice()
        print("\nComputer chose:", computer_choice_call)
        game_result = game_rule(player_choice_call,computer_choice_call)
        print("\nGame result:", game_result)

# Calling the game function
rock_paper_scissors_game()