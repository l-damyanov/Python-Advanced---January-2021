countries = input().split(', ')
cities = input().split(', ')
zipped = zip(countries, cities)
print("\n".join([f'{country} -> {city}' for country, city in zipped]))
