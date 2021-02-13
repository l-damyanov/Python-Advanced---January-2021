from collections import deque

DATURA_BOMBS_VALUE = 40
CHERRY_BOMBS_VALUE = 60
SMOKE_DECOY_BOMBS_VALUE = 120

bomb_effects = deque(list(map(int, input().split(", "))))
bomb_casings = list(map(int, input().split(", ")))

bombs = {"datura": 0, "cherry": 0, "smoke_decoy": 0}
filled_pouch = False

while len(bomb_effects) > 0 and len(bomb_casings) > 0:
    bomb_value = bomb_effects[0] + bomb_casings[-1]
    if bomb_value == DATURA_BOMBS_VALUE or bomb_value == CHERRY_BOMBS_VALUE or bomb_value == SMOKE_DECOY_BOMBS_VALUE:
        if bomb_value == DATURA_BOMBS_VALUE:
            bombs["datura"] += 1
            bomb_effects.popleft()
            bomb_casings.pop()
        elif bomb_value == CHERRY_BOMBS_VALUE:
            bombs["cherry"] += 1
            bomb_effects.popleft()
            bomb_casings.pop()
        elif bomb_value == SMOKE_DECOY_BOMBS_VALUE:
            bombs["smoke_decoy"] += 1
            bomb_effects.popleft()
            bomb_casings.pop()
        if bombs["datura"] >= 3 and bombs["cherry"] >= 3 and bombs["smoke_decoy"] >= 3:
            filled_pouch = True
    else:
        bomb_casings[-1] -= 5
    if filled_pouch == True:
        break

if bombs["datura"] >= 3 and bombs["cherry"] >= 3 and bombs["smoke_decoy"] >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for key, value in sorted(bombs.items(), key=lambda x: x[0]):
    if key == "cherry":
        print(f"Cherry Bombs: {value}")
    elif key == "datura":
        print(f"Datura Bombs: {value}")
    elif key == "smoke_decoy":
        print(f"Smoke Decoy Bombs: {value}")