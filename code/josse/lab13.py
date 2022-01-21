class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return self.name


class Game:

    def __init__(self):
        self.board = [

            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]

        ]

    def __repr__(self):
        for line in self.board:
            print("|".join(line))

    def move(self, x, y, player):
        self.board[x][y] = player.token

    def calc_winner(self, player):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == player.token:
            return player.token
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == player.token:
            return player.token
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == player.token:
            return player.token
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == player.token:
            return player.token
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == player.token:
            return player.token
        else:
            return None

    def is_full(self):

    def is_game_over(self):


def main():
    game = Game()

    player_1_name = input(f"please enter your name: ")
    player_2_name = input(f"please enter your name: ")

    player_1_token = input(f" please select x or o: ").lower()
    if player_1_token == "x":

        player_2_token = "o"
    else:
        player_2_token = "x"

    player_1 = Player(player_1_name, player_1_token)
    player_2 = Player(player_2_name, player_2_token)

    # print(player_1)


# game.move(0, 0, player_1)
# game.move(0, 1, player_2)
# print(game.__repr__())
main()
