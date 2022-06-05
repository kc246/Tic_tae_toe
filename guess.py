import random

def guess():
    upper_bound = int(input('Please enter the upper bound: '))
    lower_bound = 1
    random_number = random.randint(1, upper_bound)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between {lower_bound} and {upper_bound}: '))
        if guess < random_number:
            print('Sorry, your guess is too low. Please guess again.')
            print('\n')
            lower_bound = guess
        elif guess > random_number:
            print('Sorry, your guess is too high. Please guess again.')
            print('\n')
            upper_bound = guess

    print(f'Congratulations! You have guessed the number {random_number} correctly!!')

def computer_guess():
    lower_bound = 1
    upper_bound = int(input('Please enter the upper bound: '))
    feedback = ''
    while feedback != 'c':
        if lower_bound != upper_bound:
            guess = random.randint(lower_bound, upper_bound)
        else:
            guess = lower_bound  # could also be high b/c low = high
        
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        
        if feedback == 'h':
            upper_bound = guess - 1
        elif feedback == 'l':
            lower_bound = guess + 1

    print(f'Yay! The computer guessed your number {guess} correctly!')
