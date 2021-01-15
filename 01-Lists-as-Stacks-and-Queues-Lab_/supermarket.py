from collections import deque

END_COMMAND = "End"
PAID_COMMAND = "Paid"

names = deque()

while True:
    command = input()
    if command == END_COMMAND:
        print(f"{len(names)} people remaining.")
        break
    elif command == PAID_COMMAND:
        while names:
            print(names.popleft())
    else:
        names.append(command)
