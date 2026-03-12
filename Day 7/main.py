import random
import hangman_art
import hangman_words

lives = 6

print(hangman_art.logo3)

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
guess_length = len(chosen_word)
for position in range(guess_length):
    placeholder += "_"

game_over = False
correct_letters = []

while not game_over:


    print(f"*********{lives}/6 LIVES LEFT**********")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}!")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"*********IT WAS {chosen_word} !YOU LOSE**********")
            print("You lose.")


    if "_" not in display:
        game_over = True
        print(f"*********YOU WIN**********")


    print(hangman_art.stages[lives])
