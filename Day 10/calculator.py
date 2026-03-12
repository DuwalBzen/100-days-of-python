# Storing functions as variable name -> You can store a reference to a function as a value to a variable


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


print("Calculator")
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate():
    should_accumulate = True
    first_no = float(input("What's the first number?: "))

    while should_accumulate:
        for op in operations:
            print(op)

        operation = input("Pick an operation ")

        if operation not in operations:
            print("Invalid operation")
            break

        second_no = float(input("What's the next number?: "))

        answer = operations[operation](first_no, second_no)

        print(f"{first_no} {operation} {second_no} = {answer}")

        cont = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation ").lower()
        if cont == "y":
            first_no = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculate()




calculate()
