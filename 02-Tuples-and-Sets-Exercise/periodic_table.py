n = int(input())
unique_elements = set()

for i in range(n):
    el = input().split()
    for e in el:
        unique_elements.add(e)

for unique_el in unique_elements:
    print(unique_el)
