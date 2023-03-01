import random as r
from colorama import Fore, Style

player_card_choice_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
computer_card_choice_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

player_list = []
computer_list = []

def initial_player_card_deal():
    player_count_total = 0

    # print("\nCard list before starting the game: ", player_card_choice_list)

    for i in range(0,2):

        player_random_card = r.choice(player_card_choice_list)

        if player_random_card == 1:
           player_card_choice_list.remove(player_random_card)
           player_card_choice_list.remove('A') 
        elif player_random_card == 'A':
            player_card_choice_list.remove(player_random_card)
            player_card_choice_list.remove(1)  
        else:
            player_card_choice_list.remove(player_random_card)

        # player_card_choice_list.remove(player_random_card)
        player_list.append(player_random_card)

    for i in range(len(player_list)):
        if player_list[i] == 'J':
            player_list[i] = 10     
        if player_list[i] == 'Q':
            player_list[i] = 10          
        if player_list[i] == 'K':
            player_list[i] = 10     
        if player_list[i] == 'A':
            player_list[i] = 11        

        player_count_total += player_list[i]

    print("\nPlayer choices: ", player_list)
    # print("Player card list after starting the game: ", player_card_choice_list)
    print("Player count = ", player_count_total)
    print("\n")

    return player_count_total

def initial_computer_card_deal():
    computer_count_total = 0

    for i in range(0,2):
        computer_random_card = r.choice(computer_card_choice_list)

        if computer_random_card == 1:
           computer_card_choice_list.remove(computer_random_card)
           computer_card_choice_list.remove('A') 
        elif computer_random_card == 'A':
            computer_card_choice_list.remove(computer_random_card)
            computer_card_choice_list.remove(1)  
        else:
            computer_card_choice_list.remove(computer_random_card)
        
        # computer_card_choice_list.remove(computer_random_card)
        computer_list.append(computer_random_card)

    for i in range(len(computer_list)):
        if computer_list[i] == 'J':
            computer_list[i] = 10     
        if computer_list[i] == 'Q':
            computer_list[i] = 10          
        if computer_list[i] == 'K':
            computer_list[i] = 10     
        if computer_list[i] == 'A':
            computer_list[i] = 11        

        computer_count_total += computer_list[i]

    print("Computer choice: ", r.choice(computer_list))
    # print("Computer card list after starting the game: ", computer_card_choice_list)
    # print("Computer count = ", computer_count_total)

    return computer_count_total

def player_card_deal(player_count, player_function_count):
    index = 2

    player_random_card = r.choice(player_card_choice_list)
    player_card_choice_list.remove(player_random_card)
    player_list.append(player_random_card)

    if player_list[index + player_function_count] == 'J':
        player_list[index + player_function_count] = 10     
    if player_list[index + player_function_count] == 'Q':
        player_list[index + player_function_count] = 10          
    if player_list[index + player_function_count] == 'K':
        player_list[index + player_function_count] = 10     
    if player_list[index + player_function_count] == 'A':
        player_list[index + player_function_count] = 11  

    player_count += player_list[index + player_function_count]
    print("\nUpdated player choices: ", player_list)
    print("Upated player count = ", player_count)
    return player_count

def computer_card_deal(computer_count, computer_function_count):
    index = 2

    computer_random_card = r.choice(computer_card_choice_list)
    computer_card_choice_list.remove(computer_random_card)
    computer_list.append(computer_random_card)

    if computer_list[index + computer_function_count] == 'J':
        computer_list[index + computer_function_count] = 10     
    if computer_list[index + computer_function_count] == 'Q':
        computer_list[index + computer_function_count] = 10          
    if computer_list[index + computer_function_count] == 'K':
        computer_list[index + computer_function_count] = 10     
    if computer_list[index + computer_function_count] == 'A':
        computer_list[index + computer_function_count] = 11  

    computer_count += computer_list[index + computer_function_count]
    # print("\nUpdated computer choices: ", computer_list)
    # print("\nUpated computer count = ", computer_count)
    return computer_count    

def player_black_jack_game():

    player_function_count = 0
    player_count_update = 0

    player_count_result = initial_player_card_deal()
    computer_count_result = initial_computer_card_deal()

    if player_count_result == 21 and computer_count_result != 21:
        print("BlackJack!, You win!")
    elif player_count_result == 21 and computer_count_result == 21:
        print("It's a Draw!, You both win!")

    if player_count_result < 21:
        while(player_count_update < 21):
            hit_stand_condition = input("\nDo you want to 'Hit' or 'Stand'? ").title()
            if hit_stand_condition == "Hit":
                player_count_update = player_card_deal(player_count_result, player_function_count)
                player_count_result = player_count_update
                player_function_count += 1
            else:
                player_count_update = player_count_result                    
                break

    return player_count_update, computer_count_result

def computer_black_jack_game(computer_count_result):

    computer_function_count = 0
    computer_count_update = 0

    computer_list = [16, 17, 18, 19, 20, 21, 22]
    while_conditon_choice = r.choice(computer_list)

    while(computer_count_update <= while_conditon_choice):

        computer_count_update = computer_card_deal(computer_count_result, computer_function_count)
        computer_count_result = computer_count_update
        computer_function_count += 1

        if computer_count_update >= computer_list[0] and computer_count_update <= computer_list[6]:
            break
    
    return computer_count_update

def black_jack_game():
    result_player = player_black_jack_game()
    result_computer = computer_black_jack_game(result_player[1])

    if result_player[0] <= 21:
        print(f"\nPlayer final count: {Fore.GREEN}{result_player[0]}")
        print(Style.RESET_ALL)
    else:
        print(f"\nPlayer final count: {Fore.RED}{result_player[0]}")
        print(Style.RESET_ALL)

    if result_computer <= 21:
        print(f"Computer final count: {Fore.GREEN}{result_computer}")
        print(Style.RESET_ALL)
    else:
        print(f"Computer final count: {Fore.RED}{result_computer}")
        print(Style.RESET_ALL)

    if  result_player[0] <= 21:   
        if result_player[0] == 21 and result_computer != 21:
            print(Fore.GREEN + "\nBlackJack!, You win!\n")
            print(Style.RESET_ALL)
        elif result_player[0] == 21 and result_computer == 21:
            print(Fore.YELLOW + "\nIt's a Draw!, You both win!\n")
            print(Style.RESET_ALL)
        elif result_player[0] > result_computer:
            print(Fore.GREEN + "\nYou Win!\n")
            print(Style.RESET_ALL)
        elif result_player[0] < result_computer:
                print(Fore.RED + "\nYou lose!\n")
                print(Style.RESET_ALL)
    else:
        print(Fore.RED + "\nYou lose!\n")      
        print(Style.RESET_ALL)      
    


    return result_player[0], result_computer

final_result = black_jack_game()

