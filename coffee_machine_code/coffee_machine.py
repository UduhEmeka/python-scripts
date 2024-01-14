import os
import time
from coffee_machine_data import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0


def clear():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def reset_coffee_machine():
    """Resets the machine every time it's called"""
    while True:
        user_input = input("To turn on the coffee machine, type 'Y' for Yes or 'N' for NO: ").upper()
        if user_input == "Y":
            print("Turning on the machine...")
            time.sleep(1)
            clear()
            coffee_machine()
        elif user_input == "N":
            print("Good Bye!")
            time.sleep(2)
            break
        else:  # Error handling.
            print("Invalid input. Please type 'Y' for 'YES' or 'N' for 'NO'.")


def get_materials(user_selection):
    """Get materials required for the selected coffee."""
    water_used = MENU[user_selection]["ingredients"]["water"]
    milk_used = MENU[user_selection]["ingredients"]["milk"]
    coffee_used = MENU[user_selection]["ingredients"]["coffee"]
    money_cost = MENU[user_selection]["cost"]
    return water_used, milk_used, coffee_used, money_cost


def sufficient_resources(water_used, milk_used, coffee_used):
    """Returns True when order can be made, False if ingredients are insufficient."""
    global water, milk, coffee
    if water <= water_used:
        print("Sorry, there is not enough water.")
        return False
    elif milk <= milk_used:
        print("Sorry, there is not enough milk.")
        return False
    elif coffee <= coffee_used:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        print("processing...")
        time.sleep(1)
        return True


def process_coins():
    """Process coins and return the total earnings."""
    print("Please insert coin.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    earnings = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return earnings


def transaction_successful(earnings, money_cost):
    """Check if the transaction was successful"""
    if earnings >= money_cost:
        change = round(earnings - money_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print(f"Sorry, not enough money. ${earnings} refunded.")
        return False


def make_coffee(water_used, milk_used, coffee_used, money_cost, user_selection):
    """Makes coffee and updates resources."""
    global water, milk, coffee, money
    water -= water_used
    milk -= milk_used
    coffee -= coffee_used
    money += money_cost
    print(f"Here is your {user_selection}. ☕️ Enjoy!.")
    return water, milk, coffee, money


def print_report():
    """Print a report of current resources and earnings."""
    global water, milk, coffee, money
    print(f"Water = {water}")
    print(f"Milk = {milk}")
    print(f"Coffee = {coffee}")
    print(f"Money = {money}")


def coffee_machine():
    """Simulate the coffee machine."""
    global water, milk, coffee, money

    turn_off = False
    while not turn_off:
        user_selection = input("What would you like? espresso/latte/cappuccino: ").lower()
        
        if user_selection == "off":
            print("Shutting down the machine...")
            time.sleep(1)
            turn_off = True
        elif user_selection == "report":
            print_report()
        elif user_selection in ["espresso", "latte", "cappuccino"]:
            water_used, milk_used, coffee_used, money_cost = get_materials(user_selection)
            if sufficient_resources(water_used, milk_used, coffee_used):
                earnings = process_coins()
                if transaction_successful(earnings, money_cost):
                    make_coffee(water_used, milk_used, coffee_used, money_cost, user_selection)
        else:
            print("Please enter a valid input")


reset_coffee_machine()
