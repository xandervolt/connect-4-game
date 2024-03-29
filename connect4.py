import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def print_board(board):
    print(np.flip(board, 0))


board = create_board()
print_board(board)
game_over = False
turn = 0


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    #Check horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] and board[r][c+2]== piece and board[r][c+3] == piece:
                return True

    #Check vertical



while not game_over:
    #Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 make your selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("PLAYER 1 WINS!")
                print_board(board)
                game_over = True

    #Ask for player 2 input
    else:
        col = int(input("Player 2 make your selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("PLAYER 2 WINS!")
                print_board(board)
                game_over = True

    if not game_over:
        print_board(board)

    turn += 1
    turn = turn % 2
