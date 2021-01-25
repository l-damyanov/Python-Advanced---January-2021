def read_matrix():
    size = int(input())
    matrix = []
    for row_index in range(size):
        row = [x for x in input().split(" ")]
        matrix.append(row)
    return matrix

def get_primary_diagonal(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += int(matrix[i][i])
    return diagonal_sum

def get_secondary_diagonal(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i + j == len(matrix) - 1:
                diagonal_sum += int(matrix[i][j])
    return diagonal_sum

matrix = read_matrix()
primary = get_primary_diagonal(matrix)
secondary = get_secondary_diagonal(matrix)

result = primary - secondary

if result < 0:
    print(result * -1)
else:
    print(result)