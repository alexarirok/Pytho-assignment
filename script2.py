users = ["""Alex", "Korir", "Kiplimo", "Felex", "Abdala"""]
username = str(input("Enter your user name: "))
if username in users:
    username = input("username exist, Pick another username: ")
    users.append(username)
else:
    users.append(username)
    if len(users) > 15:
        print(users)
    break