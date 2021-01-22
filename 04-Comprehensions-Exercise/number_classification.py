numbers = list(map(int, input().split(', ')))
positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(str(el) for el in positive)}")
print(f"Negative: {', '.join(str(el) for el in negative)}")
print(f"Even: {', '.join(str(el) for el in even)}")
print(f"Odd: {', '.join(str(el) for el in odd)}")
