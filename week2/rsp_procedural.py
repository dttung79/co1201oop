import random as rd

def game_play():
    n_wins = 0
    n_looses = 0
    n_draws = 0

    n_turns = 5
    for i in range(1, n_turns + 1):
        print(f'Turn {i}')
        comp_choice = computer_choose()
        player_choice = player_choose()
        status = compare(comp_choice, player_choice)
    
        n_wins += 1 if status == 1 else 0
        n_looses += 1 if status == -1 else 0
        n_draws += 1 if status == 0 else 0
    
    print(f'Player wins: {n_wins}')
    print(f'Computer wins: {n_looses}')
    print(f'Draws: {n_draws}')

def computer_choose():
    choices = ['rock', 'scissors', 'paper']
    return rd.choice(choices)

def player_choose():
    choices = ['rock', 'scissors', 'paper']
    choice = input('Enter your choice (rock/scissors/paper): ')
    while choice not in choices:
        print('Invalid choice. Please try again.')
        choice = input('Enter your choice (rock/scissors/paper): ')
    return choice

def compare(comp_choice, player_choice):
    print(f'Player: {player_choice}, Computer: {comp_choice}')
    if comp_choice == player_choice:
        print('Draw game!')
        return 0
    if (player_choice == 'rock' and comp_choice == 'scissors') or \
        (player_choice == 'scissors' and comp_choice == 'paper') or \
        (player_choice == 'paper' and comp_choice == 'rock'):
        print('Player wins!')
        return 1
    print('Computer wins!')
    return -1

## Main program ##
game_play()