def get_magic_triangle(n):
    triangle = []
    triangle.append([1])
    triangle.append([1, 1])

    for i in range(2, n):
        triangle.append([])
        for j in range(i + 1):
            upper_right_num = 0
            upper_left_num = 0
            if i-1 < 0 or j < 0 or j > i-1:
                upper_right_num = 0
            else:
                try:
                    upper_right_num = triangle[i-1][j]
                except IndexError:
                    upper_right_num = 0

            if i-1 < 0 or j-1 < 0 or j-1 > i-1:
                upper_left_num = 0
            else:
                try:
                    upper_left_num = triangle[i-1][j-1]
                except IndexError:
                    upper_left_num = 0

            num_sum = upper_right_num + upper_left_num
            triangle[i].append(num_sum)

    return triangle

get_magic_triangle(5)