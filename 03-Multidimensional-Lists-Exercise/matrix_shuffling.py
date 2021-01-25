rows, cols = list(map(int, input().split()))

matrix = []

for _ in range(rows):
    matrix.append([el for el in input().split()])

data = input()

while data != "END":
    split_data = data.split(' ')
    if split_data[0] == "swap" and len(split_data) == 5:
        command = split_data[0]
        first_row = int(split_data[1])
        first_col = int(split_data[2])
        second_row = int(split_data[3])
        second_col = int(split_data[4])

        if (first_row and second_row) in range(rows) and (first_col and second_col) in range(cols):
            matrix[first_row][first_col], matrix[second_row][second_col] = matrix[second_row][second_col], matrix[first_row][first_col]

            for row_index in range(len(matrix)):
                print(' '.join([str(el) for el in matrix[row_index]]))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    data = input()
