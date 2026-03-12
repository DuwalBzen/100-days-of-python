


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
choice_1 = input("\tType \"left\" or \"right\" \n").lower()

if choice_1 == "left":
    print("You\'ve come to a lake. There is an island in the middle of the lake.")
    choice_2 = input(' Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if(choice_2 == "wait"):
        print("You arrive at the island unharmed. There is a house with 3 doors. \n One red, one yellow and one blue. ")
        choice_3 = input("Which colour do you choose? ").lower()
        if choice_3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice_3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choice_3 == "yellow":
            print("You found the treasure. You Win!.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("Game Over.")
