# task 5-8 Admin welcome
users = ['alice', 'bob', 'charlie', 'david', 'admin']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

# task 5-9 No users
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# task 5-10 Checking usernames
current_users = ['Alice', 'bob', 'charlie', 'david', 'alex']
new_users = ['ALICE', 'dylan', 'Charlie', 'max', 'Richard']

normalized_current = {user.lower() for user in current_users}

if new_users:
    for user in new_users:
        if user.lower() in normalized_current:
            print(f"Login {user} already in use. Please choose another one.")
        else:
            print(f"Login '{user}' is available.")
            current_users.append(user)

print(current_users)

# task 5-11 Ordinal numerals
numbers = [x for x in range(1, 10)]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")