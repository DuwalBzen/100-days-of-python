# Function



def greet():
    print("Hello ")
    print("World")
    print("Have a good day")


# Function that allow for input
# def greet_with_name(username):
#     print("Hello " + username)
#     print("World")
#     print("It's the weather great today?")
#
# greet_with_name("Bzen")

# Functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is in like your current {location}")


greet_with(location = "Bzen", name ="Inari")