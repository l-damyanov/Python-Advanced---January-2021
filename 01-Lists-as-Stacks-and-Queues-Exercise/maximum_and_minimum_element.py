n = int(input())

s = []

for _ in range(n):
    query = input().split(" ")

    if query[0] == "1":
        s.append(query[1])
    elif query[0] == "2":
        if len(s) > 0:
            s.pop()
    elif query[0] == "3":
        if len(s) > 0:
            print(max(s))
    elif query[0] == "4":
        if len(s) > 0:
            min_num = int(s[0])
            for el in s:
                if int(el) < min_num:
                    min_num = int(el)
            print(min_num)

stack = s[::-1]

print(', '.join(stack))
