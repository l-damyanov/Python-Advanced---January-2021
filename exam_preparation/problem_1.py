from collections import deque

males = list(map(int, input().split()))
females = deque(list(map(int, input().split())))

matches = 0

while len(males) > 0 and len(females) > 0:
    current_male = males[-1]
    current_female = females[0]

    if current_male <= 0:
        males.pop()
        continue
    elif current_female <= 0:
        females.popleft()
        continue

    elif current_male % 25 == 0:
        males.pop()
        if len(males) > 0:
            males.pop()
    elif current_female % 25 == 0:
        females.pop()
        if len(females) > 0:
            females.pop()

    elif current_female == current_male:
        males.pop()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if len(males) > 0:
    print(f"Males left: {', '.join([str(el) for el in males][::-1])}")
else:
    print("Males left: none")
if len(females) > 0:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")
