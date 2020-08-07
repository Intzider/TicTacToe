import random
import numpy as np


def main():
    # initialize all relevant parameters
    board = init_board()
    players = init_players()
    marks = ["X", "O"]
    active_player_index = 0
    current_player = players[active_player_index]

    # loop until there is a winner or the board is full
    while not check_for_winner(board) or not is_board_full(board):
        current_player = players[active_player_index]
        current_player_mark = marks[active_player_index]

        announce_player(current_player)
        show_board(board)
        choose_location(board, current_player_mark)

        active_player_index = (active_player_index + 1) % len(players)

    game_over_print(board, current_player)


def init_board():
    """Set board to zero"""
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def init_players():
    """Enter palyer names and randomly select starting player"""
    players = [input("Enter player name: "), input("Enter player name: ")]
    player_1 = random.choice(players)
    player_2 = players[players.index(player_1) - 1]
    print(f"{player_1} goes 1st!")
    return [player_1, player_2]


def check_for_winner(board):
    """Check after any round if there is a winner"""
    # check for winner by rows
    if check_winning_states(board):
        return True

    # check for winner by columns | transpose board
    flipped_board = np.transpose(board)
    if check_winning_states(flipped_board):
        return True

    # check for winner by diagonals
    diagonals = [
        np.diagonal(board),
        np.diagonal(np.fliplr(board))
    ]
    if check_winning_states(diagonals):
        return True


def check_winning_states(rows_to_be_checked):
    """Helper function for checking if there is a winner"""
    for row in rows_to_be_checked:
        mark = row[0]
        if mark and all(mark == cell for cell in row):
            return True


def is_board_full(board):
    """Check if board is full - used to check if there is a tie"""
    if None not in board:
        return True


def announce_player(player):
    """Announce player whose turn it is"""
    print(f"{player}, choose a field")


def show_board(board):
    """Draw current state of the board"""
    for row in board:
        for cell in row:
            cell = cell if cell is not None else "_"
            print(cell, end=" ")
        print()


def choose_location(board, mark):
    """Let current player choose spot on board"""
    location = int
    while True:
        try:
            location = int(input(f"Choose spot to put {mark} (1-9): "))
            if location in range(1, 10):
                break
        except ValueError:
            print("Spot must be between an integer between 1 and 9!")
            continue
    row, column = (location - 1) // 3, (location - 1) % 3
    if board[row][column] is not None:
        print("Please select a valid spot!")
        choose_location(board, mark)
    else:
        board[row][column] = mark
    print()


def game_over_print(board, current_player):
    """Print game result along with final board state"""
    print()
    if not check_for_winner(board):
        print("The game is a tie!")
    else:
        print(f"Game over! {current_player} won with game state: ")
    show_board(board)


if __name__ == '__main__':
    main()
