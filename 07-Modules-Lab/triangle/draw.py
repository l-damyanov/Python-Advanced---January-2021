def draw_triangle(n):
    for i in range(1, n+1):
        row = []
        for j in range(1, i+1):
            row.append(str(j))
        print(' '.join(row))

    for i in range(n-1, 0, -1):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))
        print(' '.join(row))
