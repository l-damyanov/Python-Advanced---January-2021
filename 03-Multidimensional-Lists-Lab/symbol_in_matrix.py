def read_matrix():
    size = int(input())
    matrix = []
    for rows_index in range(size):
        row = [x for x in input()]
        matrix.append(row)
    return matrix

def find_symbol(matrix, symbol):
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            current_symbol = matrix[row_index][col_index]
            if current_symbol == symbol:
                return (row_index, col_index)

def print_result(result, symbol):
    if result:
        print(result)
    else:
        print(f"{symbol} does not occur in the matrix")

matrix = read_matrix()
symbol = input()

print_result(find_symbol(matrix, symbol), symbol)