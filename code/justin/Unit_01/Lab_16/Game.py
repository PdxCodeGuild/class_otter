from Player import *
from GameBoard import *
from GameObject import *
from Token import *
from Button import *
from Utility import *


class Game:
    def __init__(self):
        self.__game_board = GameBoard()
        self.__is_player_1_turn = True
        self.__is_game_over = True
        self.__title = 'Tic-Tac-Toe'
        self.__game_objects = []
        
        self._should_quit = False
        self._player_1 = Player('Player 1', 'X')
        self._player_2 = Player('Player 2', 'O')
        self._winner = None
        self.title_text = ''

        self._title_panel = Panel(self.__title, position=Vector2(0, -200), color=GRAY)

        def play_func(self):
            self.reset()
        self._play_button = Button("PLAY", Vector2(0, 145), Vector2(240, 40), mult_color(BRIGHT_GREEN, 0.9), click_func=play_func)

        def quit_func(self):
            self._should_quit = True
        self._quit_button = Button("QUIT", Vector2(0, 195), Vector2(240, 40), mult_color(BRIGHT_RED, 0.9), click_func=quit_func)

        self._finish_game()

    def _finish_game(self):
        self.__game_objects.clear()
        self.__game_objects.append(self._title_panel)
        self.__game_objects.append(self._play_button)
        self.__game_objects.append(self._quit_button)

        winning_token = self.__game_board.calc_winner()
        if winning_token == self._player_1.token:
            self._winner = self._player_1
        elif winning_token == self._player_2.token:
            self._winner = self._player_2
        else:
            self._winner = None


    def reset(self):
        self.__game_objects.clear()

        self.__game_board = GameBoard()
        self.__is_player_1_turn = True
        self.__is_game_over = False
        self._winner = None

        self._play_button.enable()
        self._quit_button.enable()

        self.__game_objects.append(self._title_panel)
        self.__game_objects.append(self.__game_board)

    def update(self, time, display):
        if not self.__is_game_over:
            self.__is_game_over = self.__game_board.is_game_over()
            if self.__is_game_over:
                self._finish_game()

        for game_object in self.__game_objects:
            game_object.update(time, display)

    def render(self, time, display):
        if self.__is_game_over:
            if self._winner is not None:
                self.title_text = f'{self.__title}    {self._winner.name} won!'
            else:
                self.title_text = f'{self.__title}'
        else:
            # Update title bar
            name = self._player_1.name if self.__is_player_1_turn else self._player_2.name
            token = self._player_1.token if self.__is_player_1_turn else self._player_2.token
            self.title_text = f'{self.__title}    {name}\'s turn -> {token}'

        # Draw game objects
        for game_object in self.__game_objects:
            game_object.draw(time, display)

    def click(self, click_position, screen_size):
        for game_object in self.__game_objects:
            game_object.click(click_position, screen_size)

        if not self.__is_game_over:
            player = self._player_1 if self.__is_player_1_turn else self._player_2
            rect_center = self.__game_board.get_rect_center_at(click_position, screen_size)
            if self.__game_board.move(click_position, player, screen_size):
                if self.__is_player_1_turn:
                    self.__game_objects.append(Token_X(Vector2(rect_center), Vector2(64, 64), BRIGHT_ORANGE))
                else:
                    self.__game_objects.append(Token_O(Vector2(rect_center), Vector2(64, 64), BRIGHT_BLUE))
                self.__is_player_1_turn = not self.__is_player_1_turn

