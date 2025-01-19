from art import logo
print(logo+"\n")

def ingredient_cal(coffee_name):
    resources["water"] -= MENU[coffee_name]["ingredients"]["water"]
    if "milk" in MENU[coffee_name]["ingredients"]:
        resources["milk"] -= MENU[coffee_name]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_name]["ingredients"]["coffee"]

def is_sufficient(coffee_name):
    """It checks if the ingredients are sufficient to make the coffee."""
    if "milk" in MENU[coffee_name]["ingredients"]:
        if resources["water"] >= MENU[coffee_name]["ingredients"]["water"] and resources["milk"] >= MENU[coffee_name]["ingredients"]["milk"] and resources["coffee"] >= MENU[coffee_name]["ingredients"]["coffee"]:
            return True
        elif resources["water"] >= MENU[coffee_name]["ingredients"]["water"] and resources["milk"] >= MENU[coffee_name]["ingredients"]["milk"] and resources["coffee"] < MENU[coffee_name]["ingredients"]["coffee"]:
            print("Sorry! There is not enough coffee")
            return False
        elif resources["milk"] >= MENU[coffee_name]["ingredients"]["milk"] and resources["coffee"] >= MENU[coffee_name]["ingredients"]["coffee"] and resources["water"] < MENU[coffee_name]["ingredients"]["water"]:
            print("Sorry! There is not enough water")
            return False
        elif resources["water"] >= MENU[coffee_name]["ingredients"]["water"] and resources["coffee"] >= MENU[coffee_name]["ingredients"]["coffee"] and resources["milk"] < MENU[coffee_name]["ingredients"]["milk"]:
            print("Sorry! There is not enough milk")
            return False
        elif resources["water"] >= MENU[coffee_name]["ingredients"]["water"] and resources["coffee"] < MENU[coffee_name]["ingredients"]["coffee"] and resources["milk"] < MENU[coffee_name]["ingredients"]["milk"]:
            print("Sorry! There are not enough coffee and milk")
            return False
        elif resources["water"] < MENU[coffee_name]["ingredients"]["water"] and resources["coffee"] >= MENU[coffee_name]["ingredients"]["coffee"] and resources["milk"] < MENU[coffee_name]["ingredients"]["milk"]:
            print("Sorry! There are not enough water and milk")
            return False
        elif resources["water"] < MENU[coffee_name]["ingredients"]["water"] and resources["coffee"] < MENU[coffee_name]["ingredients"]["coffee"] and resources["milk"] >= MENU[coffee_name]["ingredients"]["milk"]:
            print("Sorry! There are not enough water and coffee")
            return False
        else:
            print("Sorry! There are not enough water, milk and coffee")
            return False
    else:
        if resources["water"] >= MENU[coffee_name]["ingredients"]["water"] and resources["coffee"] >= MENU[coffee_name]["ingredients"]["coffee"]:
            return True
        elif resources["water"] >= MENU[coffee_name]["ingredients"]["water"] and resources["coffee"] < MENU[coffee_name]["ingredients"]["coffee"]:
            print("Sorry! There is not enough coffee")
            return False
        elif resources["coffee"] >= MENU[coffee_name]["ingredients"]["coffee"] and resources["water"] < MENU[coffee_name]["ingredients"]["water"]:
            print("Sorry! There is not enough water")
            return False
        elif resources["water"] < MENU[coffee_name]["ingredients"]["water"] and resources["coffee"] < MENU[coffee_name]["ingredients"]["coffee"]:
            print("Sorry! There are not enough water and coffee")
            return False
        else:
            print("Sorry! There are not enough water, milk and coffee")
            return False


def print_report(current_money):
    print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${current_money}\n")

def cal_money(quarter, dime, nickle, pennie):
    return (0.25 * quarter) + (0.10 * dime) + (0.05 * nickle) + (0.01 * pennie)

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
off = False
while not off:
    # TODO: 1. Ask user for their choice
    user_choice = input("What would you like?(espresso/latte/cappuccino): ")
    if user_choice == "off":
        print("Turning off the machine...\nTurned off!")
        off = True
        continue
    if user_choice == "report":
        print_report(money)
        continue
    #TODO: 2. Check if resources sufficient
    sufficient = is_sufficient(user_choice)
    if sufficient:
        print("Insert coins")
        quarters = float(input("Quarters: "))
        dimes = float(input("Dimes: "))
        nickles = float(input("Nickles: "))
        pennies = float(input("Pennies: "))
        total_money = cal_money(quarters, dimes, nickles, pennies)
        if total_money >= MENU[user_choice]["cost"]:
            money += MENU[user_choice]["cost"]
            m_change = total_money - MENU[user_choice]["cost"]
            print(f"Here is ${m_change:.2f} in change.")
            ingredient_cal(user_choice)
            print(f"Here is your {user_choice}☕ Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
