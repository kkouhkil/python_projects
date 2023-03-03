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


def espresso_order ():
    espresso_required_water = MENU["espresso"]["ingredients"]["water"]
    espresso_required_coffee = MENU["espresso"]["ingredients"]["coffee"]

    if resources["Water (ml)"] >= espresso_required_water and resources["Coffee (g)"] >= espresso_required_coffee:
        print("Enjoy your espresso!")
        resources["Water (ml)"] = resources["Water (ml)"] - espresso_required_water
        resources["Coffee (g)"] = resources["Coffee (g)"] - espresso_required_coffee
    else:
        if resources["Water (ml)"] < espresso_required_water:
            print("Sorry, there is no enough water!")
        elif resources["Coffee (g)"] < espresso_required_coffee:
            print("Sorry, there is no enough coffee!")

def latte_order():
    latte_required_water = MENU["latte"]["ingredients"]["water"]
    latte_required_milk = MENU["latte"]["ingredients"]["milk"]
    latte_required_coffee = MENU["latte"]["ingredients"]["coffee"]

    if resources["Water (ml)"] >= latte_required_water and resources["Milk (ml)"] >= latte_required_milk and \
            resources["Coffee (g)"] >= latte_required_coffee:
        print("Enjoy your latte!")
        resources["Water (ml)"] = resources["Water (ml)"] - latte_required_water
        resources["Milk (ml)"] = resources["Milk (ml)"] - latte_required_milk
        resources["Coffee (g)"] = resources["Coffee (g)"] - latte_required_coffee
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

    if resources["Water (ml)"] >= cappuccino_required_water and resources["Milk (ml)"] >= cappuccino_required_milk and \
            resources["Coffee (g)"] >= cappuccino_required_coffee:
        print("Enjoy your latte!")
        resources["Water (ml)"] = resources["Water (ml)"] - cappuccino_required_water
        resources["Milk (ml)"] = resources["Milk (ml)"] - cappuccino_required_milk
        resources["Coffee (g)"] = resources["Coffee (g)"] - cappuccino_required_coffee
    else:
        if resources["Water (ml)"] < cappuccino_required_water:
            print("Sorry, there is no enough water!")
        elif resources["Milk (ml)"] < cappuccino_required_milk:
            print("Sorry, there is no enough milk!")
        elif resources["Coffee (g)"] < cappuccino_required_coffee:
            print("Sorry, there is no enough coffee!")

    # print(espresso_required_water, espresso_required_coffee)
    # print(resources["Water (ml)"])
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
