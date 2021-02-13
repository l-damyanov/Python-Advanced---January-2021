def check_inside_matrix(row, col):
    if not row in range(n) or not col in range(n):
        return False
    return True

def move_left(current_row, current_col, word):
    col_position = current_col - 1
    if not check_inside_matrix(current_row, col_position):
        word = word[:-1]
        return current_row, current_col, word
    else:
        current_element = matrix[current_row][col_position]
        if current_element != "-":
            word += current_element
        matrix[current_row][col_position] = "P"
        matrix[current_row][current_col] = "-"
        return current_row, col_position, word

def move_right(current_row, current_col, word):
    col_position = current_col + 1
    if not check_inside_matrix(current_row, col_position):
        word = word[:-1]
        return current_row, current_col, word
    else:
        current_element = matrix[current_row][col_position]
        if current_element != "-":
            word += current_element
        matrix[current_row][col_position] = "P"
        matrix[current_row][current_col] = "-"
        return current_row, col_position, word

def move_up(current_row, current_col, word):
    row_position = current_row - 1
    if not check_inside_matrix(row_position, current_col):
        word = word[:-1]
        return current_row, current_col, word
    else:
        current_element = matrix[row_position][current_col]
        if current_element != "-":
            word += current_element
        matrix[row_position][current_col] = "P"
        matrix[current_row][current_col] = "-"
        return row_position, current_col, word

def move_down(current_row, current_col, word):
    row_position = current_row + 1
    if not check_inside_matrix(row_position, current_col):
        word = word[:-1]
        return current_row, current_col, word
    else:
        current_element = matrix[row_position][current_col]
        if current_element != "-":
            word += current_element
        matrix[row_position][current_col] = "P"
        matrix[current_row][current_col] = "-"
        return row_position, current_col, word

move_mapper = {
    "left": move_left,
    "right": move_right,
    "up": move_up,
    "down": move_down
}

initial_string = input()
n = int(input())

matrix = []

p_row_index = None
p_col_index = None

for i in range(n):
    current_row = list(input())
    if "P" in current_row:
        p_row_index = i
        p_col_index = current_row.index("P")
    matrix.append(current_row)

n_commands = int(input())

for _ in range(n_commands):
    command = input()
    p_row_index, p_col_index, initial_string = move_mapper[command](p_row_index, p_col_index, initial_string)


print(initial_string)
for row_index in range(n):
    print("".join(matrix[row_index]))