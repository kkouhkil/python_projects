"""Author: Keyhan Kouhkiloui Babarahmati
           PhD in Robotics and AI
"""

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""

print(logo)

def add (num1, num2):
    return num1 + num2

def sub (num1, num2):
    return num1 - num2

def mul (num1, num2):
    return num1 * num2

def div (num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    count = 1
    num = float(input(f"What's you No.{count}? "))

    for key in operations:
        print(key)

    calculation_continue = True
    while(calculation_continue):
        count = count + 1
        operation_symbol = input("Pick an operation from the list above: ")

        num_rest = float(input(f"What's your No.{count}? "))

        calculation_function = operations[operation_symbol]
        answer = float(calculation_function(num, num_rest))

        print(f"{num} {operation_symbol} {num_rest} = {answer}")  

        user_ask = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: " )
        if user_ask == 'y':
            num = answer
        else:
            calculation_continue = False
            calculator()

calculator()

