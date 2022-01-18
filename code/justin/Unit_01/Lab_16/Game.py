from Player import *
from GameBoard import *
from GameObject import *
from Token import *
from Button import *


class Game:
    def __init__(self):
        self._game_board = GameBoard()
        self._is_player_1_turn = True
        self._is_game_over = False
        self._title = 'Tic-Tac-Toe'
        self._game_objects = []
        self._should_quit = False

        self.player_1 = Player('Player 1', 'X')
        self.player_2 = Player('Player 2', 'O')
        self.winner = None
        self.title_text = ''

        def quit_func(self):
            self._should_quit = True

        def play_func(self):
            self.reset()

        self.play_button = Button("Play", Vector2(0, 130), (240, 40), (32, 255, 64), click_func=play_func)
        self.quit_button = Button("Quit", Vector2(0, 175), (240, 40), (255, 64, 32), click_func=quit_func)

        self._game_objects.append(self._game_board)

    def reset(self):
        self._game_objects.clear()

        self._game_board = GameBoard()
        self._is_player_1_turn = True
        self._is_game_over = False
        self.winner = None

        self.play_button._is_disabled = False
        self.quit_button._is_disabled = False

        self._game_objects.append(self._game_board)

    def update(self, time, display):
        if not self._is_game_over:
            self._is_game_over = self._game_board.is_game_over()
            if self._is_game_over:
                self._game_objects.clear()
                self._game_objects.append(self.play_button)
                self._game_objects.append(self.quit_button)
                if self._game_board.calc_winner() == 'X':
                    self.winner = self.player_1
                else:
                    self.winner = self.player_2

        for game_object in self._game_objects:
            game_object.update(time, display)

    def render(self, time, display):
        if self._is_game_over:
            self.title_text = f'{self._title}    {self.winner.name} won!'
        else:
            # Update title bar
            name = self.player_1.name if self._is_player_1_turn else self.player_2.name
            token = self.player_1.token if self._is_player_1_turn else self.player_2.token
            self.title_text = f'{self._title}    {name}\'s turn -> {token}'

        # Draw game objects
        for game_object in self._game_objects:
            game_object.draw(time, display)

    def click(self, click_position, screen_size):
        for game_object in self._game_objects:
            game_object.click(click_position, screen_size)

        if not self._is_game_over:
            player = self.player_1 if self._is_player_1_turn else self.player_2
            rect_center = self._game_board.get_rect_center_at(click_position, screen_size)
            if self._game_board.move(click_position, player, screen_size):
                if self._is_player_1_turn:
                    self._game_objects.append(Token_X(Vector2(rect_center), Vector2(64, 64), (0, 128, 255)))
                else:
                    self._game_objects.append(Token_O(Vector2(rect_center), Vector2(64, 64), (0, 128, 255)))
                self._is_player_1_turn = not self._is_player_1_turn

