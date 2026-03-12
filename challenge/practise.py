import random

# Count Vowels
# Write a program that:
# Asks user for a string
# Counts how many vowels (a, e, i, o, u) are in it
# Prints the total
"""
in operator: The ‘in’ operator is used to check if a value
exists in a sequence or not. Evaluates to true if it finds
a variable in the specified sequence and false otherwise.


user_input = input("What is your favourite country?")
result = ""
vowels = ["a","e","i","o","u"]
for char in user_input:
    if char in vowels:
        result += char

print("The total vowel count is", len(result))
"""

"""
# 2. Number Guessing (Simple Version)
# Generate a random number between 1 and 20
# Ask user to guess
# Tell them:
# "Too high"
# "Too low"
# "Correct"
# (Only one guess for now)

user_input = int(input("Can you guess the number between 0 and 20?"))
random_number = random.randint(1,20)
print(random_number)
if user_input > random_number:
    print("You guessed too high")
elif user_input < random_number:
    print("You guessed too low")
elif user_input == random_number:
    print("You guessed correct")
else:
    print("You guessed incorrect")

"""


"""
# Reverse Without [::-1]
# Reverse a string using a loop.
# Input:
# hello
# Output:
# olleh

user_input = input("Enter a word to reverse it: ")
reversed_word = ""
for char in user_input:
    reversed_word = char + reversed_word

print(reversed_word)

"""

"""
# Remove Duplicates
nums = [1,2,2,3,4,4,5]
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)

print(unique)
"""

"""
# Level 3 – Mini Challenge (Think Like Programmer)
#Character Frequency Counter

user_input = input("Enter a word: ").lower()

chars = list(user_input)
printed = []   # to avoid duplicate printing

for char in chars:
    if char not in printed:
        print(char, ":", chars.count(char))
        printed.append(char)
        
"""

# Challenge 4
# Write a program that:
# Takes a number from user
# Checks if it is a prime number
# Prints:
# "Prime"
# "Not Prime"

user_input = int(input("Enter a no: "))
prime_no = False

for no in range(2,user_input):
    if user_input % no == 0:
       prime_no = False
       break


if prime_no:
    print(user_input, "is a prime number")
else:
    print(user_input, "is not a prime number")

