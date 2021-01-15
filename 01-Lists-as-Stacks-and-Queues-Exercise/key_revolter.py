from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(list(map(int, input().split())))
intelligence_value = int(input())

total_price = 0
done = False
while len(bullets) != 0:
    for b in range(0, gun_barrel_size + 1):
        if len(bullets) > 0:
            if b == gun_barrel_size and len(bullets) > 0:
                print("Reloading!")
                break
            if len(locks) != 0:
                current_bullet = bullets.pop()
                total_price += bullet_price
                if current_bullet <= locks[0]:
                    locks.popleft()
                    print("Bang!")
                else:
                    print("Ping!")
            elif len(locks) == 0:
                print(f"{len(bullets)} bullets left. Earned ${intelligence_value - total_price}")
                done = True
                break
            if len(bullets) == 0 and len(locks) == 0:
                print(f"{len(bullets)} bullets left. Earned ${intelligence_value - total_price}")
                done = True
                break
        else:
            break
    if done:
        break

if len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
