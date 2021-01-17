word = input()
set_word = set()

for ch in word:
    set_word.add(ch)

for ch in sorted(set_word):
    print(f"{ch}: {word.count(ch)} time/s")
