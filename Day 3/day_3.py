# Conditional Statements, Logical Operators, Code Blocks and Scope
# IF Conditional
# Modulo Operator // to check the no typed by the user is odd or even

"""
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height>120:
    print("you can ride")
else:
    print("You can't ride")
"""

# Even should divide cleanly
"""
input_no = int(input("Enter a random number"))
if input_no%2 == 0:
    print("The input number is even")
else:
    print("The input number is odd")
"""

# Nested if else Statements

height = int(input("Enter your height in cm "))
bill = 0
if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5$")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Youth tickets are 7$")
    elif age >= 45 and age <=55:
        print("Every thing is going to be ok. Have a free ride with us. ")
    else:
        bill = 12
        print("Adult tickets are 12$")
    wants_photo = input("You you want to take photo? Type y for Yes and n for No.").upper()
    if wants_photo == 'Y':
        # Add $3 to their bill
        bill += 3
    print(f"Your final tickets are {bill}$")

else:
    print("Sorry, you cannot ride the rollercoaster")



"""
# Pizza Order Practice
print("Welcome to Python  Pizza Deliveries!")

def ask_for_pepperoni(size, price):
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
    if pepperoni == 'Y':
        if size == 'S':
            price += 2
        elif size == 'M':
            price += 3
        elif size == 'L':
            price += 3
    return price

price = 0
while True:
    size = input("What size pizza do you want? S, M or L: ").upper()
    if size == 'S':
        price = 15
        break
    elif size == 'M':
        price = 20
        break
    elif size == 'L':
        price = 25
    else:
        print("You typed the wrong inputs.")

price = ask_for_pepperoni(size, price)

extra_chese = input("Do you want extra cheese? Y or N: ").upper()
if extra_chese == 'Y':
    price += 1

print(f"Your final bill is ${price}")
"""
