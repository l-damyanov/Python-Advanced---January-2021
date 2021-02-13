def read_board():
    board = []
    for _ in range(1, 8 + 1):
        board.append(input().split())
    return board

def in_range(value, max_value):
    return 0 <= value < max_value


def search_with_deltas(board, king, deltas):
    rows_count = len(board)
    columns_count = len(board[0])
    (row_index, col_index) = king
    (delta_row, delta_col) = deltas
    while in_range(row_index, rows_count) and in_range(col_index, columns_count):
        if board[row_index][col_index] == "Q":
            return (row_index, col_index)
        row_index += delta_row
        col_index += delta_col

def find_king_position(board):
    for row_index in range(len(board)):
        if "K" in board[row_index]:
            col_index = board[row_index].index("K")
            return (row_index, col_index)

def get_capturing_queens(board, king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1),
    ]
    return [
        search_with_deltas(board, king, delta)
        for delta in deltas
    ]



def print_result(queens):
    sorted_queens = []
    for q in queens:
        if q != None:
            sorted_queens.append(q)

    if sorted_queens:
        for queen in sorted_queens:
            if queen != None:
                print(f"[{', '.join([str(el) for el in queen])}]")
    else:
        print("The king is safe!")


board = read_board()
king = find_king_position(board)
queens = get_capturing_queens(board, king)
print_result(queens)

