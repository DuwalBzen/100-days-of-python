# Day 4
# Randoisation and Python List

import random

from yt_dlp.utils import caesar

#import my_module
#print(f"My favourate number is {my_module.my_favourite_number}")

# random_no = random.randint(1,6)
# random_number_0_to_1 = random.random() * 10
# print(random_no)
# print(f"The random number from 0 to 10 is {random_number_0_to_1}")


# Create a coil flipper program using random number
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")