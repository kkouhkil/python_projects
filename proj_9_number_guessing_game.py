"""Author: Keyhan Kouhkiloui Babarahmati
           PhD in Robotics and AI
"""
import random as r
from colorama import Fore, Style

UPPER_LIMIT = 100
LOWER_LIMIT = 1

def greeting():
    game_name = "Number Guessing Game"
    user_name = input("\nMay I have your name please: ")
    print(f"\nHi {Fore.CYAN}{user_name}{Style.RESET_ALL},", f"Welcome to the {Fore.YELLOW}{game_name}{Style.RESET_ALL}!")

def computer_number_guessing():
    number_list = []
    for i in range(LOWER_LIMIT,UPPER_LIMIT + 1):
        number_list.append(i)

    computer_guess = r.choice(number_list)
    print(f"I'm thinking of a number between {LOWER_LIMIT} and {UPPER_LIMIT}! Let's Play the game!")
    return computer_guess

def player_number_guess(computer_guess):
    user_lives_count = 0

    difficulty_level_select = input("\nChoose the difficulty level of 'easy', 'medium', 'hard', 'extreme' or 'nightmare': ").title()
    if difficulty_level_select == "Easy":
        user_lives_count = 15
    elif difficulty_level_select == "Medium":
        user_lives_count = 10
    elif difficulty_level_select == "Hard":
        user_lives_count = 5
    elif difficulty_level_select == "Extreme":
        user_lives_count = 3
    elif difficulty_level_select == "Nightmare":
        user_lives_count = 1
 
    if user_lives_count > 5:
        print(f"\nYou have {Fore.GREEN}{user_lives_count}{Style.RESET_ALL} attempt(s) remaining to guess the right number!, Good Luck!") 
    elif user_lives_count <= 5:
        print(f"\nYou have {Fore.RED}{user_lives_count}{Style.RESET_ALL} attempt(s) remaining to guess the right number!, Good Luck!") 
    player_number = int(input("Make a guess please: "))

    while(user_lives_count > 1):
        
        if player_number == computer_guess:
            print(f"\n{Fore.GREEN}Congratulations, You Win! (your number = {player_number}, computer number = {computer_guess}){Style.RESET_ALL}\n")
            break
        else:
            user_lives_count = user_lives_count - 1

            if player_number > computer_guess:
                print("Too High!")
            elif player_number < computer_guess:
                print("Too Low!")

            if user_lives_count > 5:
                print(f"\nYou have {Fore.GREEN}{user_lives_count}{Style.RESET_ALL} attempt(s) remaining to guess the right number!, Good Luck!") 
            elif user_lives_count <= 5:
                print(f"\nYou have {Fore.RED}{user_lives_count}{Style.RESET_ALL} attempt(s) remaining to guess the right number!, Good Luck!") 


            player_number = int(input("Make a guess please: "))

    if player_number != computer_guess:
        print(f"\n{Fore.RED}You lose!, (your number = {player_number}, computer number = {computer_guess}), Better luck next time!{Style.RESET_ALL}\n")

                

def number_guessing_game():
    greeting()

    game_continue_condition = True
    while(game_continue_condition):
        computer_number = computer_number_guessing()
        player_number_guess(computer_number)
        ask_player = input("Do you want to give the game another try: ('yes' or 'no') ")
        if ask_player == "yes":
            continue
        else:
            print(f"\n{Fore.YELLOW}Goodbye!, See you soon again!{Style.RESET_ALL}")
            game_continue_condition = False

number_guessing_game()