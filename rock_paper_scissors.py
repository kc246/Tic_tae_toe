import random
import math

def play():
    print('\n')
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    if user == 'r':
        user == 'rock'
    elif user == 'p':
        user == 'paper'
    else:
        user == 'scissors'

    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True
    return False

def play_best_of():
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
    print('\n')
    no_of_game = int(input('How many games you want to play: '))
    while no_of_game % 2 == 0: 
        print('Please enter an odd number!')
        no_of_game = int(input('How many games you want to play: '))

    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(no_of_game/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print('It is a tie. You and the computer have both chosen {}. \n'.format(user))
            print(f'Current score: You {player_wins} - {computer_wins} Computer')
        # you win
        elif result == 1:
            player_wins = player_wins + 1
            print('You chose {} and the computer chose {}. You won!\n'.format(user, computer))
            print(f'Current score: You {player_wins} - {computer_wins} Computer')
        else:
            computer_wins = computer_wins + 1
            print('You chose {} and the computer chose {}. You lost :(\n'.format(user, computer))
            print(f'Current score: You {player_wins} - {computer_wins} Computer')

    if player_wins > computer_wins:
        print('\n')
        print('You have won the best of {} games! What a champ :D'.format(no_of_game))
    else:
        print('\n')
        print('Unfortunately, the computer has won the best of {} games. Better luck next time!'.format(no_of_game))

play_best_of()
