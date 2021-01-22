bunker = {category: [] for category in input().split(', ')}
n = int(input())
bunker['all_items_count'] = 0
bunker['all_quality'] = 0

for _ in range(n):
    category, item_name, values = input().split(' - ')
    item_quantity = int(values.split(';')[0].split(':')[1])
    item_quality = int(values.split(';')[1].split(':')[1])
    item_data = {item_name: {'quantity': item_quantity, 'quality': item_quality}}
    bunker[category].append(item_data)
    bunker['all_items_count'] += item_quantity
    bunker['all_quality'] += item_quality

print(f"Count of items: {bunker['all_items_count']}")
print(f"Average quality: {bunker['all_quality']/(len(bunker) - 2):.2f}")
print(*[f"{category} -> {', '.join([list(d.keys())[0] for d in value])}" for category, value in bunker.items() if isinstance(bunker[category], list)], sep="\n")
