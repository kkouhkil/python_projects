"""Author: Keyhan Kouhkiloui Babarahmati
           PhD in Robotics and AI
"""

import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print("\n<<< Welcome to Secret Auction Program >>>")
print(logo)

secret_auction_dict = {}

def secret_auction_dict_creation():
    secret_auction_continue = True

    while(secret_auction_continue):
        key = input("What is your name? ")
        value = input("What is your bid? $")
        secret_auction_dict[key] = float(value)
        
        continue_bid_condition = input("Are there any other biders? ('Yes' or 'No') ").lower()

        if continue_bid_condition == "yes":
            os.system('clear')
            continue
        else:
            secret_auction_continue = False

    return secret_auction_dict

def secret_auction_program(secret_auction_dict):
    key_list = []
    value_list = []
    max_bid = 0
    bid_winner = ""
    
    for key in secret_auction_dict:
        key_list.append(key)
        value_list.append(secret_auction_dict[key])

    if len(value_list) == 1:
        max_bid = value_list[0]
    else:

        for i in range(1, len(value_list)):
            if value_list[i - 1] > value_list[i]:
                max_bid = value_list[i - 1]
            else:
                max_bid = value_list[i]

    bid_winner = key_list[value_list.index(max_bid)]

    print(f"The winner is {bid_winner} with the maximum bid of ${max_bid}")

secret_auction_dict_result = secret_auction_dict_creation()

for key in secret_auction_dict_result:
    print(f"Bidder: {key}, ", f"Bid = ${secret_auction_dict_result[key]}")

secret_auction_program(secret_auction_dict)

        