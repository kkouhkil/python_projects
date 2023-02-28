import random as r

player_card_choice_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
computer_card_choice_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

player_list = []
computer_list = []

def initial_player_card_deal():
    player_count_total = 0

    print("\nCard list before starting the game: ", player_card_choice_list)

    for i in range(0,2):

        player_random_card = r.choice(player_card_choice_list)
        player_card_choice_list.remove(player_random_card)
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

    print("Player choices: ", player_list)
    print("Player card list after starting the game: ", player_card_choice_list)
    print("Player count = ", player_count_total)
    print("\n")

    return player_count_total

def initial_computer_card_deal():
    computer_count_total = 0

    for i in range(0,2):
        computer_random_card = r.choice(computer_card_choice_list)
        computer_card_choice_list.remove(computer_random_card)
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

    print("Computer choices: ", computer_list)
    print("Computer card list after starting the game: ", computer_card_choice_list)
    print("Computer count = ", computer_count_total)

    return computer_count_total

player_count_result = initial_player_card_deal()
computer_count_result = initial_computer_card_deal()

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

    player_count += player_list[index]
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

    computer_count += computer_list[index]
    print("\nUpdated computer choices: ", computer_list)
    print("Upated computer count = ", computer_count)
    return computer_count    

player_card_deal(player_count_result, 0)
computer_card_deal(computer_count_result, 0)




