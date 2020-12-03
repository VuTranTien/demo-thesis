# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import enum
import random
from functools import reduce


class Cell(enum.Enum): #use to determine player too
    MAN = 1 #player
    AI = 0 # AI
    EMPTY = -1


class GameResult(enum.Enum):
    loss = 1
    draw = 2
    win = 3


class GameState:
    def __init__(self, N, src = []):
        self.N = N
        self.is_over = False
        if len(src) == 0:
            self.board = [[Cell.EMPTY for i in range(0, self.N)] for j in range(0, self.N)]
        else:
            self.board = src

    def legal_moves(self):
        lst = []
        for i in range(0, self.N):
            for j in range(0, self.N):
                if self.board[i][j] == Cell.EMPTY:
                    lst.append(self.board[i][j])
        return lst

    def apply_move(self, move, player):
        self.board[move[0]][move[1]] = Cell.AI if player == Cell.AI else Cell.MAN
        return GameState(self.N, self.board)

    def is_over(self):
        return self.is_over

    def next_player(self):

        pass


    def prinBoard(self):
        for i in range(0, self.N):
            print(str([self.board[i][j].value for j in range(0, self.N)]))


class MinimaxAgent:

    def select_move(self, game_state):
        winning_move = []
        draw_move = []
        losing_move = []
        for possible_move in game_state.legal_moves():
            next_state = game_state.apply_move(possible_move)
            opponent_best_outcome = best_result(next_state)
            out_best_outcome = reverse_game_result(opponent_best_outcome)

            if out_best_outcome == GameResult.win:
                winning_move.append(possible_move)
            elif out_best_outcome == GameResult.draw:
                draw_move.append(possible_move)
            else:
                losing_move.append(possible_move)
        if winning_move:
            return random.choice(draw_move)
        if draw_move:
            return random.choice(draw_move)
        return random.choice(losing_move)


def reverse_game_result(state):
    return 0


def best_result(game_state):
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return GameResult.win
        elif game_state.winner() is None:
            return GameResult.draw
        else:
            return GameResult.loss

    best_result_so_far = GameResult.loss
    for candidate_move in game_state.legal_moves():
        next_state = game_state.apply_move(candidate_move)
        opponent_best_result = best_result(next_state)
        our_result = reverse_game_result(opponent_best_result)
        if our_result.value > best_result_so_far.value:
            best_result_so_far = our_result

    return best_result_so_far


def print_hi(name):
    gst = GameState(3)
    print(gst.prinBoard())
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} ')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
