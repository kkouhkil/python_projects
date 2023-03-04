"""Author: Keyhan Kouhkiloui Babarahmati
           PhD in Robotics and AI
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "Water (ml)": 300,
    "Milk (ml)": 200,
    "Coffee (g)": 100,
    "Money ($)": float(0)
}


def espresso_order():
    espresso_required_water = MENU["espresso"]["ingredients"]["water"]
    espresso_required_coffee = MENU["espresso"]["ingredients"]["coffee"]
    espresso_cost = MENU["espresso"]["cost"]

    if resources["Water (ml)"] >= espresso_required_water and resources["Coffee (g)"] >= espresso_required_coffee:
        espresso_coin_counter = coin_counter()
        if espresso_coin_counter < espresso_cost:
            print("Sorry, that's not enough money. Money refunded!")
        else:
            print("Enjoy your espresso!")
            print(f'Your change is: {espresso_coin_counter - espresso_cost}')
            resources["Water (ml)"] = resources["Water (ml)"] - espresso_required_water
            resources["Coffee (g)"] = resources["Coffee (g)"] - espresso_required_coffee
            resources["Money ($)"] = resources["Money ($)"] + espresso_cost
    else:
        if resources["Water (ml)"] < espresso_required_water:
            print("Sorry, there is no enough water!")
        elif resources["Coffee (g)"] < espresso_required_coffee:
            print("Sorry, there is no enough coffee!")


def latte_order():
    latte_required_water = MENU["latte"]["ingredients"]["water"]
    latte_required_milk = MENU["latte"]["ingredients"]["milk"]
    latte_required_coffee = MENU["latte"]["ingredients"]["coffee"]
    latte_cost = MENU["latte"]["cost"]

    if resources["Water (ml)"] >= latte_required_water and resources["Milk (ml)"] >= latte_required_milk and \
            resources["Coffee (g)"] >= latte_required_coffee:
        latte_coin_counter = coin_counter()
        if latte_coin_counter < latte_cost:
            print("Sorry, that's not enough money. Money refunded!")
        else:
            print("Enjoy your latte!")
            print(f'Your change is: {latte_coin_counter - latte_cost}')
            resources["Water (ml)"] = resources["Water (ml)"] - latte_required_water
            resources["Milk (ml)"] = resources["Milk (ml)"] - latte_required_milk
            resources["Coffee (g)"] = resources["Coffee (g)"] - latte_required_coffee
            resources["Money ($)"] = resources["Money ($)"] + latte_cost
    else:
        if resources["Water (ml)"] < latte_required_water:
            print("Sorry, there is no enough water!")
        elif resources["Milk (ml)"] < latte_required_milk:
            print("Sorry, there is no enough milk!")
        elif resources["Coffee (g)"] < latte_required_coffee:
            print("Sorry, there is no enough coffee!")


def cappuccino_order():
    cappuccino_required_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_required_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_required_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    cappuccino_cost = MENU["cappuccino"]["cost"]

    if resources["Water (ml)"] >= cappuccino_required_water and resources["Milk (ml)"] >= cappuccino_required_milk and \
            resources["Coffee (g)"] >= cappuccino_required_coffee:
        cappuccino_coin_counter = coin_counter()
        if cappuccino_coin_counter < cappuccino_cost:
            print("Sorry, that's not enough money. Money refunded!")
        else:
            print("Enjoy your cappuccino!")
            print(f'Your change is: {cappuccino_coin_counter - cappuccino_cost}')
            resources["Water (ml)"] = resources["Water (ml)"] - cappuccino_required_water
            resources["Milk (ml)"] = resources["Milk (ml)"] - cappuccino_required_milk
            resources["Coffee (g)"] = resources["Coffee (g)"] - cappuccino_required_coffee
            resources["Money ($)"] = resources["Money ($)"] + cappuccino_cost
    else:
        if resources["Water (ml)"] < cappuccino_required_water:
            print("Sorry, there is no enough water!")
        elif resources["Milk (ml)"] < cappuccino_required_milk:
            print("Sorry, there is no enough milk!")
        elif resources["Coffee (g)"] < cappuccino_required_coffee:
            print("Sorry, there is no enough coffee!")


def coin_counter():
    quarters = 0.25
    dime = 0.10
    nickle = 0.05
    penny = 0.01

    print("Please insert coins to continue")
    quarters_count = int(input("How many quarters: "))
    dimes_count = int(input("How many dimes: "))
    nickles_count = int(input("How many nickles: "))
    pennies_count = int(input("How many pennies: "))

    total_inserted_change = quarters_count * quarters + dimes_count * dime + \
        nickles_count * nickle + pennies_count * penny

    return total_inserted_change


def report():
    for key in resources:
        print(f"{key}: {resources[key]}")


def coffee_machine():
    while(True):
        user_input = input("What would you like to have? (espresso, latte or cappuccino) ").lower()
        if user_input == "espresso":
            espresso_order()
        elif user_input == "latte":
            latte_order()
        elif user_input == "cappuccino":
            cappuccino_order()
        elif user_input == "report":
            report()
        elif user_input == 'off':
            print("The coffee machine is turned off!")
            break


coffee_machine()
# print(MENU)
# print(resources)
