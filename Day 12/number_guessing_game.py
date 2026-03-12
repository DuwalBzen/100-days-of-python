import random


random_number = random.randint(1, 100)
game_difficulty = {
    "easy" : 10,
    "hard" : 5
}

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Psst, the correct answer is {random_number}.")

continue_game = True

game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if game_level == "easy":
    print(f"You have attempts {game_difficulty["easy"]} remaining to guess the number.")
elif game_level == "hard":
    print(f"You have attempts {game_difficulty["hard"]} remaining to guess the number.")


while game_difficulty[game_level] != 0:
    make_guess = int(input("Make a guess: "))
    if make_guess < random_number:
        game_difficulty[game_level] -= 1
        print('Too low!\n'
              'Guess again.\n'
              f'You have {game_difficulty[game_level]} attempts remaining to guess the number.')
    elif make_guess > random_number:
        game_difficulty[game_level] -= 1
        print('Too high!\n'
              'Guess again.\n'
              f'You have {game_difficulty[game_level]} attempts remaining to guess the number.')
    elif make_guess == random_number:
        print("You got it! The number was " + str(random_number))
        game_difficulty[game_level] = 0

if game_difficulty[game_level] == 0:
    print('You loose!')
