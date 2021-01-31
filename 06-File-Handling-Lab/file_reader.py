with open("numbers.txt", "r") as file:
    print(sum([int(el.strip("\n")) for el in file.readlines()]))
