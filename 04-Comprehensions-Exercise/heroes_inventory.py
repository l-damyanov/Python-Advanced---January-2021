def update_heroes(name, item, price, heroes):
    if not heroes[name].get(item):
        heroes[name].update({item: int(price)})

    return heroes

names = input().split(', ')

data = input()
heroes = {name: {} for name in names}

while data != "End":
    name, item, price = data.split('-')

    heroes = update_heroes(name, item, price, heroes)

    data = input()

print(*[f"{name} -> Items: {len(items)}, Cost: {sum([price for item, price in items.items()])}" for name, items in heroes.items()], sep="\n")
