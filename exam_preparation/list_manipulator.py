def list_manipulator(list_nums, *args):
    command = args[0]
    position = args[1]

    if command == "add":
        if position == "beginning" and len(args) > 2:
            counter = 0
            for i in range(2, len(args)):
                list_nums.insert(counter, args[i])
                counter += 1
        elif position == "end" and len(args) > 2:
            for i in range(2, len(args)):
                list_nums.append(args[i])

    elif command == "remove":
        if position == "beginning" and len(args) > 2:
            n = args[2]
            for _ in range(n):
                list_nums.pop(0)
        elif position == "beginning" and len(args) == 2:
            list_nums.pop(0)
        elif position == "end" and len(args) > 2:
            n = args[2]
            for _ in range(n):
                list_nums.pop()
        elif position == "end" and len(args) == 2:
            list_nums.pop()

    return list_nums


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
