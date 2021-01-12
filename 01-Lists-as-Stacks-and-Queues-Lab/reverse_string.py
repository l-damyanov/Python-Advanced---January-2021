text = input()

s = []

for el in text:
    s.append(el)

result = ""

while s:
    result += s.pop()
print(result)