n = int(input())

intersections = []

for _ in range(n):
    data = input()
    first_sequence_data, second_sequence_data = data.split("-")
    start, stop = [int(el) for el in first_sequence_data.split(",")]
    first_sequence = range(start, stop + 1)
    start, stop = [int(el) for el in second_sequence_data.split(",")]
    second_sequence = range(start, stop + 1)
    intersection = set(first_sequence).intersection(second_sequence)
    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))[0]
print(f"Longest intersection is {list(longest)} with length {len(longest)}")
