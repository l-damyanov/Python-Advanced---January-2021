text = input()

vowels = {'a', 'o', 'u', 'e', 'i'}
[vowels.add(x.upper()) for x in list(vowels)]


result = [str(el) for el in text if el not in vowels]
print(''.join(result))
