command = input()
phone_book = {}

while len(command) > 1:
    name, phone_number = command.split("-")
    if name not in phone_book:
        phone_book[name] = phone_number
    phone_book[name] = phone_number

    command = input()

n = 0

if command.isdigit():
    n += int(command)

for i in range(n):
    contact_name = input()
    if contact_name in phone_book:
        print(f"{contact_name} -> {phone_book[contact_name]}")
    else:
        print(f"Contact {contact_name} does not exist.")
