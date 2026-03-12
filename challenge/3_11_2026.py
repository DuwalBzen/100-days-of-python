# Day 17 Challenge: Python Bank System

account = {
    "name": "Bzen",
    "balance": 1000,
    "transactions": []
}


def deposit(account, amount):
    if amount > 0:
        account["balance"] += amount
        account["transactions"].append(f"Deposited ${amount}")

def withdrawal(account, amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        account["transactions"].append("withdrawal $" + str(amount))
    else:
        print("Insufficient balance")

def get_transactions(transactions):
    print("Your transaction history")
    for t in transactions:
        print(t + "\n")

is_continue = True

while is_continue:
    print("Welcome to Python Bank")
    menu = int(input('1. Deposit\n'
                     '2. Withdraw\n'
                     '3. Check Balance\n'
                     '4. Transaction History\n'
                     '5. Exit\n'))

    # Task 1 — Deposit Money
    if menu == 1:
        amount = int(input('Enter amount to deposit : $'))
        deposit(account, amount)

    # Task 2 — Withdraw Money
    elif menu == 2:
        withdrawal_amount = int(input('Enter amount to withdrawal : $'))
        withdrawal(account, withdrawal_amount)


    elif menu == 3:
        print(f"Your current balance is $ {account["balance"]}")

    elif menu == 4:
        user_transactions = account["transactions"]
        get_transactions(user_transactions)


    elif menu == 5:
        print("Thank you for using Python Bank.")
        is_continue = False

    else:
        print("Invalid option")