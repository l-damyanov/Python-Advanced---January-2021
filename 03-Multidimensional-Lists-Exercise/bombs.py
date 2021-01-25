size = int(input())

rows = size
cols = size
matrix = []
active_cells = 0
total_sum = 0

for row_index in range(size):
    matrix.append(list(map(int, input().split())))

coordinates = [tuple(map(int, el.split(','))) for el in input().split(' ')]

for el in coordinates:
    row = el[0]
    col = el[1]
    if matrix[row][col] > 0:
        try:
            if matrix[row-1][col-1] > 0 and row-1 >=0 and col-1 >= 0:
                matrix[row-1][col-1] -= matrix[row][col]
        except:
            IndexError

        try:
            if matrix[row-1][col] > 0 and row-1 >=0 and col >= 0:
                matrix[row-1][col] -= matrix[row][col]
        except:
            IndexError

        try:
            if matrix[row-1][col+1] > 0 and row-1 >=0 and col+1 >= 0:
                matrix[row-1][col+1] -= matrix[row][col]
        except:
            IndexError

        try:
            if matrix[row][col-1] > 0 and row >=0 and col-1 >= 0:
                matrix[row][col-1] -= matrix[row][col]
        except:
            IndexError

        try:
            if matrix[row][col+1] > 0 and row >=0 and col+1 >= 0:
                matrix[row][col+1] -= matrix[row][col]
        except:
            IndexError

        try:
            if matrix[row+1][col-1] > 0 and row+1 >=0 and col-1 >= 0:
                matrix[row+1][col-1] -= matrix[row][col]
        except:
            IndexError

        try:
            if matrix[row+1][col] > 0 and row+1 >=0 and col >= 0:
                matrix[row+1][col] -= matrix[row][col]
        except:
            IndexError

        try:
            if matrix[row+1][col+1] > 0 and row+1 >=0 and col+1 >= 0:
                matrix[row+1][col+1] -= matrix[row][col]
        except:
            IndexError

        matrix[row][col] = 0

for r in matrix:
    for c in r:
        if c > 0:
            active_cells += 1
            total_sum += c

print(f"Alive cells: {active_cells}")
print(f"Sum: {total_sum}")
[print(' '.join(str(el) for el in i)) for i in matrix]
