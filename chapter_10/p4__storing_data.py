import json

from settings import TEXT_DIR

# Using json.dump() and json.load()

numbers = [i for i in range(0, 20, 2)]

filename = "numbers.json"

# write in file
with open(TEXT_DIR / filename, "w") as f:
    json.dump(numbers, f)

# read from file
with open(TEXT_DIR / filename) as f:
    numbers_from_file = json.load(f)

print(numbers_from_file)

# Saving and Reading User-Generated Data
# remember_me
username = input("What is your name? ")

filename = "username.json"
with open(TEXT_DIR / filename, "w") as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

# greet_user
with open(TEXT_DIR / filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = "username.json"

try:
    with open(TEXT_DIR / filename) as f:
        username = json.load(f)

except FileNotFoundError:
    username = input("What is your name? ")

    with open(TEXT_DIR / filename, "w") as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")

else:
    print(f"Welcome back, {username}!")


# Refactoring
def get_stored_username():
    """Get stored username if available."""
    filename = "username.json"

    try:
        with open(TEXT_DIR / filename) as f:
            username = json.load(f)

    except FileNotFoundError:
        return None

    else:
        return username


def get_new_user():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = "username.json"

    with open(TEXT_DIR / filename, "w") as f:
        json.dump(username, f)

    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_user()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
