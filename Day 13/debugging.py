# The process of removing bugs from the code


def my_function():
    for i in range(1,20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# The problem is that it is not printing "you got it"

# 1. What is the loop doing?
# 2. When is the function meant to print "You got it"
# 3. What are your assumptions about the value of i


# Reproduce the Bug
# Some bugs are sneaky, they only occur under certain conditions. In order to debug them, we need to be able to reluably reproduce the bug and diagnose our problem to figure out which conditions tigger the bug.
from random import randint
dice_image = ["1","2","3","4","5","6"]
dice_number = randint(1,6)
print(dice_image[dice_number])

# Play computer
"""
playing computer is an important skill in debugging.
You need to be able to go through your code line by line as 
if you were the computer
"""

year = int(input("What year were you born? "))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")