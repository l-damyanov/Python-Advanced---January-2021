rows, cols = [int(el) for el in input().split()]

result = [[f"{chr(num)}{chr(nested_num)}{chr(num)}" for nested_num in range(num, num + cols)] for num in range(97, 97 + rows)]

print(*[' '.join(iterable) for iterable in result], sep='\n')
