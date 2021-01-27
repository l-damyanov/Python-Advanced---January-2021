def print_odd(nums):
    return (sum(el for el in nums if el % 2 != 0)) * len(nums)

def print_even(nums):
    return (sum(el for el in nums if el % 2 == 0)) * len(nums)


command = input()
numbers = list(map(int, input().split()))

if command == "Odd":
    print(print_odd(numbers))
elif command == "Even":
    print(print_even(numbers))
