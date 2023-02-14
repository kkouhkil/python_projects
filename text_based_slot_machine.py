MIN_BET = float(1)

def get_deposit():
    deposit_satisfaction = bool(True)
    while(deposit_satisfaction):
        deposit_amount = input("Enter the amount of money you want to deposit: $")
        try:
            float(deposit_amount)
            if float(deposit_amount) > 0:
                deposit_satisfaction = bool(False)
            else:
                print("Wrong input!, Enter a positive amount greater than zero and try again!")
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

def bet_on_each_line(deposit_amount):
    bet_on_each_line_satisfaction = bool(True)
    while(bet_on_each_line_satisfaction):
        bet_on_each_line = input("Enter the amount of bet you want to have for each line: $")
        try:
            float(bet_on_each_line)
            if float(bet_on_each_line) >= MIN_BET and float(bet_on_each_line) <= deposit_amount:
                bet_on_each_line_satisfaction = bool(False)
            else:
                print("Wrong input!, Enter a positive amount between " + str(MIN_BET) + " and " + str(deposit_amount) + "! Try again!")
        except:
            print("Wrong input!, Enter the acceptable amonut in terms of numbers!")
            bet_on_each_line_satisfaction = bool(True)
    
    return float(bet_on_each_line)



def main():
    get_deposit_call = get_deposit()
    get_number_of_lines_call = get_number_of_lines()
    bet_on_each_line_call = bet_on_each_line(get_deposit_call)
    print("Your deposited amount is: $", get_deposit_call)
    print("Number of lines you selected to bet on is: " + str(get_number_of_lines_call) + " line(s)")
    print("The bet amount you entered for each line is: $", bet_on_each_line_call)

main()