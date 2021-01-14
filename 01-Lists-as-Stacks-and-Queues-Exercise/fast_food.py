from collections import deque

total_food = int(input())
order = list(map(int, input().split()))
quantity_order = deque()

for el in order:
    quantity_order.append(el)

print(max(quantity_order))


while len(quantity_order) > 0:
    if total_food >= quantity_order[0]:
        total_food -= quantity_order[0]
        quantity_order.popleft()
    else:
        print(f"Orders left: {' '.join([str(el) for el in quantity_order])}")
        break

if len(quantity_order) == 0:
    print("Orders complete")
