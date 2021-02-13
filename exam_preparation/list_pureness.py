def best_list_pureness(*args):
    numbers = args[0]
    counter = args[1]
    values = []
    value = 0
    for i in range(len(numbers)):
        value += numbers[i] * i
    values.append(value)
    for _ in range(counter):
        numbers.insert(0, numbers[-1])
        numbers.pop()
        value = 0
        for i in range(len(numbers)):
            value += numbers[i] * i
        values.append(value)

    best_pureness = 0
    best_index = 0
    for el in values:
        if el > best_pureness:
            best_pureness = el
            best_index = values.index(el)

    return f"Best pureness {best_pureness} after {best_index} rotations"

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
