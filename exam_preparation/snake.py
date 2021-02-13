def check_inside_territory(row, col):
    if not row in range(size) or not col in range(size):
        return False
    return True

def check_if_burrow(row, col):
    if snake_territory[row][col] == "B":
        return True
    return False

size = int(input())

snake_territory = []
s_row_index = None
s_col_index = None

for i in range(size):
    current_row = list(input())
    if "S" in current_row:
        s_row_index = i
        s_col_index = current_row.index("S")
    snake_territory.append(current_row)

snake_in_territory = True
total_food = 0

while snake_in_territory and total_food < 10:
    burrow = False
    command = input()

    if command == "up":
        burrow = False
        if not check_inside_territory(s_row_index - 1, s_col_index):
            snake_in_territory = False
            snake_territory[s_row_index][s_col_index] = "."
            break
        if snake_territory[s_row_index - 1][s_col_index] == "*":
            total_food += 1
        if check_if_burrow(s_row_index - 1, s_col_index) == True:
            burrow = True
            snake_territory[s_row_index][s_col_index] = "."
            snake_territory[s_row_index - 1][s_col_index] = "."
            for row_i in range(size):
                for col_i in range(size):
                    if snake_territory[row_i][col_i] == "B":
                        snake_territory[row_i][col_i] = "S"
                        s_row_index = row_i
                        s_col_index = col_i
                        break
        if burrow == False:
            snake_territory[s_row_index][s_col_index] = "."
            snake_territory[s_row_index - 1][s_col_index] = "S"
            s_row_index = s_row_index - 1

    elif command == "down":
        burrow = False
        if not check_inside_territory(s_row_index + 1, s_col_index):
            snake_in_territory = False
            snake_territory[s_row_index][s_col_index] = "."
            break
        if snake_territory[s_row_index + 1][s_col_index] == "*":
            total_food += 1
        if check_if_burrow(s_row_index + 1, s_col_index) == True:
            burrow = True
            snake_territory[s_row_index][s_col_index] = "."
            snake_territory[s_row_index + 1][s_col_index] = "."
            for row_i in range(size):
                for col_i in range(size):
                    if snake_territory[row_i][col_i] == "B":
                        snake_territory[row_i][col_i] = "S"
                        s_row_index = row_i
                        s_col_index = col_i
                        break
        if burrow == False:
            snake_territory[s_row_index][s_col_index] = "."
            snake_territory[s_row_index + 1][s_col_index] = "S"
            s_row_index = s_row_index + 1

    elif command == "left":
        burrow = False
        if not check_inside_territory(s_row_index, s_col_index - 1):
            snake_in_territory = False
            snake_territory[s_row_index][s_col_index] = "."
            break
        if snake_territory[s_row_index][s_col_index - 1] == "*":
            total_food += 1
        if check_if_burrow(s_row_index, s_col_index - 1) == True:
            burrow = True
            snake_territory[s_row_index][s_col_index] = "."
            snake_territory[s_row_index][s_col_index - 1] = "."
            for row_i in range(size):
                for col_i in range(size):
                    if snake_territory[row_i][col_i] == "B":
                        snake_territory[row_i][col_i] = "S"
                        s_row_index = row_i
                        s_col_index = col_i
                        break
        if burrow == False:
            snake_territory[s_row_index][s_col_index] = "."
            snake_territory[s_row_index][s_col_index - 1] = "S"
            s_col_index = s_col_index - 1

    elif command == "right":
        burrow = False
        if not check_inside_territory(s_row_index, s_col_index + 1):
            snake_in_territory = False
            snake_territory[s_row_index][s_col_index] = "."
            break
        if snake_territory[s_row_index][s_col_index + 1] == "*":
            total_food += 1
        if check_if_burrow(s_row_index, s_col_index + 1) == True:
            burrow = True
            snake_territory[s_row_index][s_col_index] = "."
            snake_territory[s_row_index][s_col_index + 1] = "."
            for row_i in range(size):
                for col_i in range(size):
                    if snake_territory[row_i][col_i] == "B":
                        snake_territory[row_i][col_i] = "S"
                        s_row_index = row_i
                        s_col_index = col_i
                        break
        if burrow == False:
            snake_territory[s_row_index][s_col_index] = "."
            snake_territory[s_row_index][s_col_index + 1] = "S"
            s_col_index = s_col_index + 1

if snake_in_territory == False:
    print("Game over!")
    print(f"Food eaten: {total_food}")

    for row in snake_territory:
        print(''.join(str(el) for el in row))

else:
    print("You won! You fed the snake.")
    print(f"Food eaten: {total_food}")

    for row in snake_territory:
        print(''.join(str(el) for el in row))