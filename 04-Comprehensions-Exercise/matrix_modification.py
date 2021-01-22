size = int(input())
matrix = []
for row_index in range(size):
    matrix.append(list(map(int, input().split())))

data = input()

while data != "END":
    command, row, col, value = data.split()
    row = int(row)
    col = int(col)
    value = int(value)

    if command == "Add":
        if 0 <= row < size and 0 <= col < size:
            matrix[row][col] += value
        else:
            print("Invalid coordinates")

    elif command == "Subtract":
        if 0 <= row < size and 0 <= col < size:
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    data = input()

print(*[' '.join([str(el) for el in row]) for row in matrix], sep="\n")
