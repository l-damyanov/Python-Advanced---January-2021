n = int(input())
usernames = set()

for el in range(n):
    user = input()
    usernames.add(user)

for username in usernames:
    print(username)
