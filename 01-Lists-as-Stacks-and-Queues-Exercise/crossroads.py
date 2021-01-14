# from collections import deque
#
# green_light_duration = int(input())
# free_window_duration = int(input())
#
# command = input()
#
# cars = deque()
# passed_cars = 0
# crashed = False
# green_light = False
# no_time = False
# while command != "END":
#
#     if command != "green":
#         cars.append(command)
#     else:
#         green_light = True
#         current_green_duration = green_light_duration
#         current_free_window_duration = free_window_duration
#         while green_light:
#             current_cars = list(cars)
#             for car in current_cars:
#                 for i in range(len(car)):
#                     if current_green_duration > 0:
#                         current_green_duration -= 1
#                         if car[i] == car[-1]:
#                             cars.popleft()
#                             passed_cars += 1
#                     elif current_green_duration == 0 and len(cars[0]) > current_free_window_duration and i == 0:
#                         no_time = True
#                         break
#                     elif current_green_duration == 0 and current_free_window_duration > 0:
#                         current_free_window_duration -= 1
#                         if car[i] == car[-1]:
#                             cars.popleft()
#                             passed_cars += 1
#                     elif current_green_duration == 0 and current_free_window_duration == 0:
#                         print(f"A crash happened!")
#                         print(f"{car} was hit at {car[i]}.")
#                         crashed = True
#                         break
#             if len(current_cars) == 0 and no_time == False:
#                 break
#             elif no_time == True:
#                 break
#             elif crashed == True:
#                 break
#         if crashed == True:
#             break
#
#     command = input()
#
# if not crashed:
#     print("Everyone is safe.")
#     print(f"{passed_cars} total cars passed the crossroads.")

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