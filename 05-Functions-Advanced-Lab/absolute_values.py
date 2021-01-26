def create_absolute_value(nums):
    result = [abs(el) for el in nums]
    return result

numbers = [float(el) for el in input().split()]
print(create_absolute_value(numbers))
