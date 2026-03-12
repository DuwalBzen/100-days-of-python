"""
Day 2
Data types, Numbers, Operators, Type conversion, f-string
"""

#The method of pulling out particular element from string is called
#subscripting "Bzen"[0]
#print("Hello"[4])

# Integer = Are the whole numbers without the decimal points
#print(40+44)
#Large Integer 984,393,1918
#print(984_393_1918)
# Float = Floating points numbers
#print(3030.33)

# Boolean True or False
#print(True)

"""
Check the data type of any function using the type functions
name = "Bzen"
salary = 10.5
mobile_no = 9843931918
is_engineer = True
print(type(name),type(salary),type(mobile_no),type(is_engineer))
"""

# Type conversion : You can convert data inot different data type using the special functions
#no_1 = int("22")
#no_2 = int("22")
#print(no_1 + no_2)
#print("Number of letters in your name: " + str(len(input("Enter your name"))))

# mathmeticals operators of python
# add, subtractions, divisions, default is float // for int // exponents by **
# Orders of mathmeticals by PEMDASLR
#print(9-3+1)

"""
# Number Manipulation
bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi,2))
"""

# Assignment operators
num = 4
num = num + 1
print(num)
num += 1
print(num)

# f-string We can use f-string to insert a variable or an expression into a string
score = 0
height = 1.8
is_winning  = True
print(f"Your score is = {score}, your height is {height}, you are wining is {is_winning}")


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many peole to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2 )

print(f"Each person should pay: ${final_amount}")
