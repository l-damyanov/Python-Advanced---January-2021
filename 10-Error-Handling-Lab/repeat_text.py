def repeat_text(text, count):
    try:
        return text * int(count)
    except ValueError:
        return ("Variable times must be an integer")

word = input()
n = input()

print(repeat_text(word, n))
