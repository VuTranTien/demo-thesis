# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import enum
import random


class GameResult(enum.Enum) :
    loss = 1
    draw = 2
    win = 3

class MinimaxAgent:
    def select_move(selfself, game_state):
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
def best_result(next_state):
    return 0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
