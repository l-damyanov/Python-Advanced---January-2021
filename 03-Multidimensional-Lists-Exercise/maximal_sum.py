rows, cols = list(map(int, input().split()))

maximal_sum = 0
matrix = []
matrix_copy = []
row = 0
col = 0

for el in range(rows):
    matrix.append([int(el) for el in input().split()])

for i in range(rows - 2):
    for j in range(cols - 2):
        sum_elements = sum([matrix[i][j], matrix[i][j+1], matrix[i][j+2], matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2], matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]])

        if sum_elements > maximal_sum:
            maximal_sum = sum_elements
            row = i
            col = j

matrix_copy = [[matrix[row][col], matrix[row][col+1], matrix[row][col+2]], [matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]], [matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]]

print(f"Sum = {maximal_sum}")
for row_index in range(len(matrix_copy)):
    print(' '.join([str(el) for el in matrix_copy[row_index]]))