import random
from random import choices

cho = ('r', 'p', 's')
computer_choice = random.choice(cho)
user_choice = input('Rock, Paper, or Scissors? (r/p/s):' ).lower()
if user_choice not in cho:
    print('Invalid choice!')

    computer_choice = random.choice(cho)
    print(f'You chose{user_choice}')
    print(f'Computer chose{computer_choice}')

if user_choice == computer_choice:
    print('Tie')
elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'r' and computer_choice == 's')):
    print('You win!')
else:
    print('You loose!')