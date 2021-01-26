def round_nums(nums):
    result = [round(el) for el in nums]
    return result

numbers = [float(el) for el in input().split()]
print(round_nums(numbers))
