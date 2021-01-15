numbers = input().split(" ")

reversed_nums = ""

while len(numbers) > 0:
    if len(numbers) > 1:
        reversed_nums += numbers.pop()
        reversed_nums += " "
    elif len(numbers) == 1:
        reversed_nums += numbers.pop()

print(reversed_nums)
