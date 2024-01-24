import random as rd

class Player:
    def __init__(self):
        self.wins = 0
    
    def choose(self):
        choices = ['rock', 'scissors', 'paper']
        choice = input('Enter your choice (rock/scissors/paper): ')
        while choice not in choices:
            print('Invalid choice. Please try again.')
            choice = input('Enter your choice (rock/scissors/paper): ')
        return choice

class Computer:
    def __init__(self):
        self.wins = 0
    
    def choose(self):
        choices = ['rock', 'scissors', 'paper']
        return rd.choice(choices)

class Game:
    def __init__(self, turns):
        self.player = Player()
        self.computer = Computer()
        self.n_turns = turns
    
    def play(self):
        for i in range(1, self.n_turns + 1):
            print(f'Turn {i}')
            comp_choice = self.computer.choose()
            player_choice = self.player.choose()
            status = self.compare(comp_choice, player_choice)
        
            self.player.wins += 1 if status == 1 else 0
            self.computer.wins += 1 if status == -1 else 0
        
        print(f'Player wins: {self.player.wins}')
        print(f'Computer wins: {self.computer.wins}')
        print(f'Draws: {self.n_turns - self.player.wins - self.computer.wins}')
    
    def compare(self, comp_choice, player_choice):
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
game = Game(5)
game.play()