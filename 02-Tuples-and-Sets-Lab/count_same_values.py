values = (map(float, input().split()))

values_count = {}
for value in values:
    if value not in values_count:
        values_count[value] = 0
    values_count[value] += 1

for (value, count) in values_count.items():
    print(f"{value} - {count} times")