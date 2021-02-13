n = int(input())
n_bombs = int(input())

matrix = []

for row_i in range(n):
    matrix.append([])
    for col_i in range(n):
        matrix[row_i].append('0')

for _ in range(n_bombs):
    coordinates = list(map(int, input().strip('()').split(', ')))
    matrix[coordinates[0]][coordinates[1]] = "*"


for row_i in range(len(matrix)):
    for col_i in range(len(matrix[row_i])):
        if matrix[row_i][col_i] != "*":
            matrix[row_i][col_i] = 0
            try:
                if matrix[row_i][col_i - 1] == "*" and col_i - 1 >= 0:
                    matrix[row_i][col_i] += 1
            except IndexError:
                pass
            try:
                if matrix[row_i][col_i + 1] == "*":
                    matrix[row_i][col_i] += 1
            except IndexError:
                pass
            try:
                if matrix[row_i - 1][col_i] == "*" and row_i - 1 >= 0:
                    matrix[row_i][col_i] += 1
            except IndexError:
                pass
            try:
                if matrix[row_i + 1][col_i] == "*":
                    matrix[row_i][col_i] += 1
            except IndexError:
                pass
            try:
                if matrix[row_i - 1][col_i - 1] == "*" and col_i - 1 >= 0 and row_i - 1 >= 0:
                    matrix[row_i][col_i] += 1
            except IndexError:
                pass
            try:
                if matrix[row_i - 1][col_i + 1] == "*" and row_i - 1 >= 0:
                    matrix[row_i][col_i] += 1
            except IndexError:
                pass
            try:
                if matrix[row_i + 1][col_i - 1] == "*" and col_i - 1 >= 0:
                    matrix[row_i][col_i] += 1
            except IndexError:
                pass
            try:
                if matrix[row_i + 1][col_i + 1] == "*":
                    matrix[row_i][col_i] += 1
            except IndexError:
                pass

for row in matrix:
    print(' '.join([str(el) for el in row]))