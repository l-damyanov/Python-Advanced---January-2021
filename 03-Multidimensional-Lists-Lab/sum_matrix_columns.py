def read_matrix():
    (rows, columns) = map(int, input().split(", "))
    matrix = []
    for rows_index in range(rows):
        row = list(map(int, input().split(" ")))
        matrix.append(row)
    return matrix

def get_column_sum(matrix):
    rows_count = len(matrix)
    columns_counts = len(matrix[0])

    sums = []
    for column_index in range(columns_counts):
        sums.append(0)
        for rows_index in range(rows_count):
            sums[-1] += matrix[rows_index][column_index]
    return sums

def print_result(values):
    for x in values:
        print(x)

matrix = read_matrix()
result = get_column_sum(matrix)
print_result(result)
