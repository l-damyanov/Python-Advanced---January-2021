from math import log

x = int(input())
base = input()

if base == "natural":
    print(f"{log(x):.2f}")
else:
    print(f"{log(x, int(base)):.2f}")
