
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

coins = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}

def report():
    """Display a report of the amount of each
    resource and money in the coffee machine"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${profit:.2f}')

profit = 0
is_on = True

# Task 1 -> "Prompt user by asking What would you like? (espresso/latte/cappuccino):"


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient ."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def make_coffee(user_choice):
    drink = MENU[user_choice]
    if is_resource_sufficient(drink["ingredients"]):
        payment = process_coins()
        is_transaction_successful(payment, drink["cost"])
        making_coffee(user_choice, drink["ingredients"])

def making_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")



def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.10
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change:} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def coffee_machine():
    """Prompts the user for a drink name if the user types 'off'
    returns otherwise the function is recalled recursively"""
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        return
    if user_choice == 'report':
        report()
    else:
        make_coffee(user_choice)

while is_on:
    coffee_machine()


