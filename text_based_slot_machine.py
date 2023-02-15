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

def get_number_of_lines():
    get_number_of_lines_satisfaction = bool(True)
    while(get_number_of_lines_satisfaction):
        number_of_lines = input("Enter the number of lines you want to bet please: ")
        try:
            int(number_of_lines)
            if int(number_of_lines) > 0:
                get_number_of_lines_satisfaction = bool(False)
            else:
                print("Wrong input!, Enter a positive amount greater than zero and try again!")
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

# PART IN PROGRESS
def slot_machine_algorithm(number_of_lines):
    symbol_count_dict = {"A" : 1 * COL_COUNT * number_of_lines, 
                    "K" : 2 * COL_COUNT * number_of_lines,
                    "Q" : 3 * COL_COUNT * number_of_lines,
                    "J" : 4 * COL_COUNT * number_of_lines
                    }
    
    all_symbols = []
    for symbol, symbol_count in symbol_count_dict.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    print("All Symbols Array = ", all_symbols)

    slot_machine_row = number_of_lines
    slot_machine_col = COL_COUNT

    slot_machine_matrix = [[0 for col in range(slot_machine_col)] for row in range(slot_machine_row)]
    print("Symbol Machine = ", slot_machine_matrix[0:number_of_lines][:])

    pass


def main():

    get_deposit_call = get_deposit()
    get_number_of_lines_call = get_number_of_lines()
    bet_on_each_line_call = bet_on_each_line(get_deposit_call, get_number_of_lines_call)
    total_bet = get_number_of_lines_call * bet_on_each_line_call
    print(f"\nTotal deposit = ${get_deposit_call}\nNumber of line(s) = {get_number_of_lines_call} \nBet for each line = ${bet_on_each_line_call} \nTotal bet = ${total_bet} \nBalance = ${get_deposit_call - total_bet}")

    # PART IN PROGRESS
    slot_machine_algorithm(get_number_of_lines_call)

main()