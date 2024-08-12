import numpy as np

def initialize_board():
    """Create a 3x3 board initialized with spaces."""
    return np.full((3, 3), ' ')

def print_board(board):
    """Print the board in a readable format."""
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

def check_win(board, player):
    """Check if the specified player has won."""
    # Check rows and columns
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True
    # Check diagonals
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def check_draw(board):
    """Check if the board is full and there's no winner."""
    return np.all(board != ' ') and not (check_win(board, 'X') or check_win(board, 'O'))

def make_move(board, row, col, player):
    """Place the player's mark on the board if the cell is empty."""
    if board[row, col] == ' ':
        board[row, col] = player
        return True
    return False

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = initialize_board()
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers 0, 1, or 2.")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and make_move(board, row, col, player):
            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("Invalid move. Try again.")

tic_tac_toe()
