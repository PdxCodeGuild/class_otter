from Player import *
from GameBoard import *


class Game:
    def __init__(self):
        self.player_1 = Player('Player 1', 'X')
        self.player_2 = Player('Player 2', 'O')
        self.game_board = GameBoard()
        self.is_player_1_turn = True
        self.title = 'Tic-Tac-Toe'
        self.title_text = ''
        pass

    def update(self):
        pass

    def render(self):
        # Update FPS in titlebar
        name = self.player_1.name if self.is_player_1_turn else self.player_2.name
        token = self.player_1.token if self.is_player_1_turn else self.player_2.token
        self.title_text = f'{self.title}    {name}\'s turn -> {token}'
        
        pass