from collections import deque

customers = deque(list(map(int, input().split(", "))))
taxis = list(map(int, input().split(", ")))
total_time = sum(customers)

while len(customers) > 0 and len(taxis) > 0:
    if customers[0] <= taxis[-1]:
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if len(customers) > 0 and len(taxis) == 0:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(el) for el in customers])}")
elif len(customers) == 0 and len(taxis) >= 0:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
