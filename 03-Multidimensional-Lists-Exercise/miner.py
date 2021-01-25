size = int(input())
directions = input().split()
rows = size
cols = size
matrix = []
total_coals = 0
collected_coals = 0
game_over = False

for i in range(rows):
    matrix.append(input().split())

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 'c':
            total_coals += 1

starting_point = ()

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == 's':
            starting_point = row_index, col_index
            break

start_row = starting_point[0]
start_col = starting_point[1]

for el in directions:
    if el == "up":
        try:
            if 0 <= start_row - 1 < size and 0 <= start_col < size:
                start_row -= 1
                start_col = start_col
                if matrix[start_row][start_col] == 'c':
                    total_coals -= 1
                    collected_coals += 1
                    matrix[start_row][start_col] = "*"
                    if total_coals <= 0:
                        print(f"You collected all coals! {start_row, start_col}")
                        game_over = True
                        break
                elif matrix[start_row][start_col] == 'e':
                    print(f"Game over! {start_row, start_col}")
                    game_over = True
                    break
        except:
            IndexError


    if el == "down":
        try:
            if 0 <= start_row + 1 < size and 0 <= start_col < size:
                start_row += 1
                start_col = start_col
                if matrix[start_row][start_col] == 'c':
                    total_coals -= 1
                    collected_coals += 1
                    matrix[start_row][start_col] = "*"
                    if total_coals <= 0:
                        print(f"You collected all coals! {start_row, start_col}")
                        game_over = True
                        break
                elif matrix[start_row][start_col] == 'e':
                    print(f"Game over! {start_row, start_col}")
                    game_over = True
                    break
        except:
            IndexError


    if el == "right":
        try:
            if 0 <= start_row < size and 0 <= start_col + 1 < size:
                start_row = start_row
                start_col += 1
                if matrix[start_row][start_col] == 'c':
                    total_coals -= 1
                    collected_coals += 1
                    matrix[start_row][start_col] = "*"
                    if total_coals <= 0:
                        print(f"You collected all coals! {start_row, start_col}")
                        game_over = True
                        break
                elif matrix[start_row][start_col] == 'e':
                    print(f"Game over! {start_row, start_col}")
                    game_over = True
                    break
        except:
            IndexError


    if el == "left":
        try:
            if 0 <= start_row < size and 0 <= start_col - 1 < size:
                start_row = start_row
                start_col -= 1
                if matrix[start_row][start_col] == 'c':
                    total_coals -= 1
                    collected_coals += 1
                    matrix[start_row][start_col] = "*"
                    if total_coals <= 0:
                        print(f"You collected all coals! {start_row, start_col}")
                        game_over = True
                        break
                elif matrix[start_row][start_col] == 'e':
                    print(f"Game over! {start_row, start_col}")
                    game_over = True
                    break
        except:
            IndexError


if game_over == False:
    print(f"{total_coals} coals left. {start_row, start_col}")
