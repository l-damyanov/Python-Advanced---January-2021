from collections import deque

START_COMMAND = "Start"
END_COMMAND = "End"
REFILL_COMMAND = "refill"
litres = int(input())

people = deque()

while True:
    command = input()
    if command == START_COMMAND:
        break
    else:
        people.append(command)

while True:
    command = input()
    if command == END_COMMAND:
        print(f"{litres} liters left")
        break
    if command.startswith(REFILL_COMMAND):
        command_params = command.split(' ')
        refill_litres = int(command_params[1])
        litres += refill_litres
    else:
        person = people.popleft()
        person_litres = int(command)
        if person_litres <= litres:
            litres -= person_litres
            print(f"{person} got water")
        else:
            print(f"{person} must wait")