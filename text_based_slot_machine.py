import random as r

MIN_DEPOSIT = float(5)
MIN_BET = float(1)

COL_COUNT = 3

def get_deposit():
    deposit_satisfaction = bool(True)
    while(deposit_satisfaction):
        deposit_amount = input("\nEnter the amount of money you want to deposit: $")
        try:
            float(deposit_amount)
            if float(deposit_amount) >= MIN_DEPOSIT:
                deposit_satisfaction = bool(False)
            else:
                print("Wrong input!, Enter a minimum amount of $" + str(MIN_DEPOSIT) +  " and try again!")
        except:
            print("Wrong input!, Enter the acceptable amonut in terms of numbers!")
            deposit_satisfaction = bool(True)


    return float(deposit_amount)

def get_number_of_lines(deposit_amount):
    get_number_of_lines_satisfaction = bool(True)
    while(get_number_of_lines_satisfaction):
        number_of_lines = input("Enter the number of lines you want to bet please: ")
        try:
            int(number_of_lines)
            if int(number_of_lines) > 0 and int(number_of_lines) < int(deposit_amount):
                get_number_of_lines_satisfaction = bool(False)
            else:
                print(f"Wrong input!, Enter a positive amount between {0} and {int(deposit_amount)}, Try again!")
        except:
            print("Wrong input!, Enter the acceptable number of lines!")
            get_number_of_lines_satisfaction = bool(True)

    return int(number_of_lines)

def bet_on_each_line(deposit_amount, number_of_lines):
    bet_on_each_line_satisfaction = bool(True)
    while(bet_on_each_line_satisfaction):
        bet_on_each_line = input("Enter the amount of bet you want to have for each line: $")
        try:
            float(bet_on_each_line)
            max_bet = float(bet_on_each_line) * float(number_of_lines)
            if float(bet_on_each_line) >= MIN_BET and max_bet <= deposit_amount:
                bet_on_each_line_satisfaction = bool(False)
            else:
                print("Wrong input!, Your overdraft is $" + str(deposit_amount - max_bet) + ", Not sufficient fund, Try again!")
        except:
            print("Wrong input!, Enter the acceptable amonut in terms of numbers!")
            bet_on_each_line_satisfaction = bool(True)

    return float(bet_on_each_line)

def slot_machine_algorithm(number_of_lines, bet_on_each_line, deposit_amount):
    symbol_count_dict = {"A" : 1 * COL_COUNT * number_of_lines, 
                    "K" : 2 * COL_COUNT * number_of_lines,
                    "Q" : 3 * COL_COUNT * number_of_lines,
                    "J" : 4 * COL_COUNT * number_of_lines
                    }
    
    # Creatign an array of all symbols w.r.t number of lines and columns 
    all_symbols = []
    for symbol, symbol_count in symbol_count_dict.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    # print("All Symbols Array = ", all_symbols)

    # Creating a 2D matrix of slot machine w.r.t number of lines and columns
    slot_machine_row = number_of_lines
    slot_machine_col = COL_COUNT

    slot_machine_matrix = [[0 for col in range(slot_machine_col)] for row in range(slot_machine_row)]
    # print("Symbol Machine = ", slot_machine_matrix[:][:])

    for i in range(slot_machine_row):
        for j in range(slot_machine_col):
            slot_machine_matrix[i][j] = r.choice(all_symbols) 
            
    print("\nGenerated line(s) by slot machine: ", slot_machine_matrix)

    # Checking the winning scenario      
    line_A_won_count = 0
    line_K_won_count = 0
    line_Q_won_count = 0
    line_J_won_count = 0

    line_A_win_amonut = 0
    line_K_win_amonut = 0
    line_Q_win_amonut = 0
    line_J_win_amonut = 0
    total_win_amount = 0

    for i in range(slot_machine_row):
        if all(element == "A" for element in slot_machine_matrix[i][:]) == True:
            line_A_won_count +=1
        if all(element == "K" for element in slot_machine_matrix[i][:]) == True:
            line_K_won_count +=1    
        if all(element == "Q" for element in slot_machine_matrix[i][:]) == True:
            line_Q_won_count +=1
        if all(element == "J" for element in slot_machine_matrix[i][:]) == True:
            line_J_won_count +=1      

    # Total number of line(s) won
    total_line_won_count = line_A_won_count + line_K_won_count + line_Q_won_count + line_J_won_count

    # Total win amount
    if line_A_won_count >= 1:
        line_A_win_amonut += line_A_won_count * bet_on_each_line * 5
    if line_K_won_count >= 1:
        line_K_win_amonut += line_K_won_count * bet_on_each_line * 4   
    if line_Q_won_count >= 1:
        line_Q_win_amonut += line_Q_won_count * bet_on_each_line * 3
    if line_J_won_count >= 1:
        line_J_win_amonut += line_J_won_count * bet_on_each_line * 2

    total_win_amount = line_A_win_amonut + line_K_win_amonut + line_Q_win_amonut + line_J_win_amonut
    
    if line_A_won_count == 0 and  line_K_won_count == 0 and line_Q_won_count == 0 and line_J_won_count == 0:
        print(f"\nUnfortunately you did not win anything. Better luck next time!")

    if  line_A_won_count != 0 or  line_K_won_count != 0 or line_Q_won_count != 0 or line_J_won_count != 0:  
        print(f"\nCongratulations!, Number of winning lines: {total_line_won_count}")
        print(f"\nYou have just won ${total_win_amount}")  

    remaining_balance = deposit_amount - (number_of_lines * bet_on_each_line)

    if total_win_amount > 0:
        print(f"Balance = ${remaining_balance + total_win_amount}\n")  
    else:
        print(f"Balance = ${remaining_balance}\n")  
    
    return float(remaining_balance)

def main():

    get_deposit_call = get_deposit()
    get_number_of_lines_call = get_number_of_lines(get_deposit_call)
    bet_on_each_line_call = bet_on_each_line(get_deposit_call, get_number_of_lines_call)
    total_bet = get_number_of_lines_call * bet_on_each_line_call
    print(f"\nTotal deposit = ${get_deposit_call}\nNumber of line(s) = {get_number_of_lines_call} \nBet for each line = ${bet_on_each_line_call} \nTotal bet = ${total_bet} \nBalance = ${get_deposit_call - total_bet}")
    new_balance = float(slot_machine_algorithm(get_number_of_lines_call, bet_on_each_line_call, get_deposit_call))


while(True):
    main()
    print("\nEnd of Text-Based Slot Machine Game")