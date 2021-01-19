def read_matrix():
    (rows, columns) = map(int, input().split(", "))
    matrix = []
    for rows_index in range(rows):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix

matrix = read_matrix()

matrix_sum = 0

for r in range(len(matrix)):
    row = matrix[r]
    row_sum = 0
    matrix_sum += sum(row)

    matrix_sum += row_sum

print(matrix_sum)
print(matrix)