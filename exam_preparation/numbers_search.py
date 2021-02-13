def numbers_searching(*args):
    numbers = list(map(int, args))
    duplicates = []
    numbers_check = []
    value = None

    for n in numbers:
        if n not in numbers_check:
            numbers_check.append(n)
        elif n in numbers_check and n not in duplicates:
            duplicates.append(n)
    sorted_numbers = sorted(numbers_check)
    sorted_duplicates = sorted(duplicates)
    if sorted_numbers:
        value = sorted_numbers[0] + 1
        while sorted_numbers[0] < value < sorted_numbers[-1]:
            if value in sorted_numbers:
                value += 1
            else:
                break
    return [value, sorted_duplicates]


print(numbers_searching(1, 2, 5, 4))
# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))