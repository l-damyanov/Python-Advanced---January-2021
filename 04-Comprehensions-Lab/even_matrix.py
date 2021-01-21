def read_matrix():
    rows_count = int(input())
    return [map(int, input().split(', ')) for _ in range(rows_count)]

matrix = read_matrix()
even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
print(even_matrix)
