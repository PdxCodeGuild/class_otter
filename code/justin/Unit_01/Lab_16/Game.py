from Player import *
from GameBoard import *
from GameObject import *
from Token import *


class Game:
    def __init__(self):
        self._game_board = GameBoard()
        self._is_player_1_turn = True
        self._title = 'Tic-Tac-Toe'
        self._game_objects = []

        self.player_1 = Player('Player 1', 'X')
        self.player_2 = Player('Player 2', 'O')
        self.title_text = ''

        self._game_objects.append(Token_X(Vector2(320, 240), Size(64, 64), (0, 128, 255)))
        self._game_objects.append(Token_Y(Vector2(320, 240), Size(64, 64), (0, 128, 255)))

    def update(self, time):
        for game_object in self._game_objects:
            game_object.update(time)

    def render(self, time):
        # Update title bar
        name = self.player_1.name if self._is_player_1_turn else self.player_2.name
        token = self.player_1.token if self._is_player_1_turn else self.player_2.token
        self.title_text = f'{self._title}    {name}\'s turn -> {token}'