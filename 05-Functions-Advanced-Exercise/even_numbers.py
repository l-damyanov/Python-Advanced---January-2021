numbers = list(map(int, input().split()))

is_even = lambda x: x % 2 == 0

filtered_nums = list(filter(is_even, numbers))
print(filtered_nums)
