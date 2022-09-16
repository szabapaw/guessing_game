import random
from art import logo
from replit import clear
def game():
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5
    answer = random.randint(1, 100)
    # print(f'Pssst the answer is: {answer}')
    should_continue = True
    while should_continue:
        print(f'You have {lives} attempts remaining to guess the number.')
        quess = int(input('Make a guess: '))
        if quess == answer:
            print(f'You win. The answer is: {answer}')
            should_continue=False
        elif quess > answer:
            print('Too high.')
            print('Guess again.')
            lives = lives- 1
        elif quess < answer:
            print('Too low.')
            print('Guess again.')
            lives = lives- 1
        if lives==0:
            print(f'You have {lives} lives. So you have no lives. You lose, but I can reveal a secret. The answer is: {answer} ')
            should_continue=False
    if input('Wanna play again in Number Guessing Game?:')=='yes':
        clear()
        game()


if input('Type yes if you want play Number Guessing Game or no if you don\'t want to play: ')=='yes':
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    game()
else:
    print('Goodbye')

