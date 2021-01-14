from collections import deque

cups_capacity = deque(list(map(int, input().split())))
bottles = list(map(int, input().split()))
wasted_water = 0

while len(cups_capacity) != 0 and len(bottles) != 0:
    current_bottle = bottles.pop()

    if cups_capacity[0] - current_bottle == 0:
        cups_capacity.popleft()
    elif cups_capacity[0] - current_bottle < 0:
        wasted_water += current_bottle - cups_capacity[0]
        cups_capacity.popleft()
    elif cups_capacity[0] - current_bottle > 0:
        cups_capacity[0] -= current_bottle

if len(cups_capacity) != 0 and len(bottles) == 0:
    print(f"Cups: {' '.join([str(el) for el in cups_capacity])}")
    print(f"Wasted litters of water: {wasted_water}")
elif len(cups_capacity) == 0 and len(bottles) != 0:
    bottles = bottles[::-1]
    print(f"Bottles: {' '.join([str(el) for el in bottles])}")
    print(f"Wasted litters of water: {wasted_water}")