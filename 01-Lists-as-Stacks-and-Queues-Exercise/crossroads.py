from collections import deque

green_time_duration = int(input())
free_time_duration = int(input())

cars = deque()

cars_passed = 0

while True:
    command = input()

    if command == "END":
        break

    if command == "green":
        current_green_time = int(green_time_duration)
        while current_green_time != 0 and cars:

            current_car = cars.popleft()
            if current_green_time - len(current_car) >= 0:
                current_green_time -= len(current_car)
                cars_passed += 1

            else:
                if (current_green_time + free_time_duration) - len(current_car) >= 0:
                    cars_passed += 1
                    break

                else:
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[(current_green_time + free_time_duration) - len(current_car)]}.")
                    exit()

        continue

    cars.append(command)

print("Everyone is safe.")
print(f"{cars_passed} total cars passed the crossroads.")
