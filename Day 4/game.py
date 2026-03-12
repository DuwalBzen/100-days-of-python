import random




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game = [rock, paper, scissors]


user_input = int(input('What do you choose?'
              'Type 0 for Rock, '
              '1 for Paper or 2 for Scissors.'))

random_generator = random.randint(0,2)

if user_input >=0 and user_input <=2 :
    print(game[user_input])

print('Computer chose:')
print(game[random_generator])


if user_input >=3 or user_input <=0 :
    print("You typed an invalid number. You lose")
elif user_input == 0 and random_generator == 1:
    print('You lose!')
elif user_input == 1 and random_generator == 2:
    print('You lose!')
elif user_input == 2 and random_generator == 0:
    print('You lose!')
elif user_input ==  random_generator:
    print('Draw!')
else:
    print('You win!')