size = int(input())
matrix = [[col for col in input().split(', ')] for row in range(size)]
first_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[i][-(i+1)] for i in range(len(matrix))]

print(f"First diagonal: {', '.join(first_diagonal)}. Sum: {sum([int(el) for el in first_diagonal])}")
print(f"Second diagonal: {', '.join(second_diagonal)}. Sum: {sum([int(el) for el in second_diagonal])}")
