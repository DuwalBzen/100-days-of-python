import string
import random

letters = list(string.ascii_lowercase)
numbers = list(string.digits)          # 0-9
symbols = list(string.punctuation)



print("Welcome to the PyPassword Generator!")
letters_no = int(input("How many letters would you like in your password?\n"))
symbols_no = int(input("How many symbols would you like\n"))
numbers_no = int(input("How many numbers would you like\n"))

# Easy Level
# password = ""
# for char in range(0, letters_no):
#     password += random.choice(letters)
#
# for i in range(0, numbers_no):
#     password += random.choice(symbols)
#
# for i in range(0, symbols_no):
#     password += random.choice(numbers)
#
# print(f"Your password is: {password}")

# Hard Level
password_list = []
for char in range(0, letters_no):
    password_list.append(random.choice(letters))

for i in range(0, numbers_no):
    password_list.append(random.choice(symbols))

for i in range(0, symbols_no):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
