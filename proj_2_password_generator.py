#Password Generator Project
import random

random_letters = ""
random_numbers = ""
random_symbols = ""

order_not_randomised_password = ""
order_randomised_password = ""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_numbers = int(input(f"How many numbers would you like? "))
nr_symbols = int(input(f"How many symbols would you like? "))

for i in range(0,nr_letters):
    # print("Your random number for LETTERS is: " + str(random.randint(0,len(letters)-1)))
    random_letters += letters[random.randint(0,len(letters)-1)]

for i in range(0,nr_numbers):
    # print("Your random number for NUMBERS is: " + str(random.randint(0,len(numbers)-1)))
    random_numbers += numbers[random.randint(0,len(numbers)-1)]

for i in range(0,nr_symbols):
    # print("Your random number for SYMBOLS is: " + str(random.randint(0,len(symbols)-1)))
    random_symbols += symbols[random.randint(0,len(symbols)-1)]

#Easy Level - Order not randomised:
order_not_randomised_password = random_letters + random_symbols + random_numbers
print("Your Password is: " + order_not_randomised_password + " ==> (order NOT randomized: letters - symbols - numbers)")

#Hard Level - Order of characters randomised:
order_not_randomised_password_list = []
order_not_randomised_password_list_shuffle = []

for i in range(0,len(order_not_randomised_password)):
    order_not_randomised_password_list += order_not_randomised_password[i]

for i in range(0,len(order_not_randomised_password)):
    random.shuffle(order_not_randomised_password_list)

for i in range(0, len(order_not_randomised_password)):
    order_randomised_password += order_not_randomised_password_list[i]

print("Your Password is: " + order_randomised_password + " ==> (order randomized!)")

#All together random password
# random_letters_numbers_symbols = letters + numbers + symbols
# nr_letters_numbers_symbols = nr_letters + nr_numbers + nr_symbols

# for i in range(0,nr_letters_numbers_symbols):
#     # print("Your random number for LETTERS/NUMBERS/SYMBOLS is: " + str(random.randint(0,len(random_letters_numbers_symbols)-1)))
#     order_randomised_password += random_letters_numbers_symbols[random.randint(0,len(random_letters_numbers_symbols)-1)]

# print("Your Password is: " + order_randomised_password + " ==> (order randomized!)")
