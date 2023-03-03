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
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": float(0)
}

def report():
    pass

report()
# print(MENU)
# print(resources)
