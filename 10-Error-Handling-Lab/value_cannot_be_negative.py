class ValueCannotBeNegativeError(Exception):
    pass

def validate_numbers(numbers):
    for number in numbers:
        if number < 0:
            raise ValueCannotBeNegativeError(f"{number} is negative")

numbers = []
for _ in range(5):
    numbers.append(int(input()))

validate_numbers(numbers)
print("Numbers are positive")
