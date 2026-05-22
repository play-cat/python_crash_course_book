# task 10-11, 10-12 Favorite Number
import json

from settings import TEXT_DIR

FILE_PATH = TEXT_DIR / "favorite_number.json"


def favorite_number():
    favorite_num = get_favorite_number()
    if favorite_num:
        print(f"I know your favorite number! It's: {favorite_num}")
    else:
        favorite_num = new_favorite_number()
        print(f"I remembered your favorite number! It's: {favorite_num}")


def new_favorite_number():
    favorite_num = input("What is your favorite number? ")

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(favorite_num, f)

    return favorite_num


def get_favorite_number():
    try:
        with open(FILE_PATH, encoding="utf-8") as f:
            favorite_num = json.load(f)

    except FileNotFoundError:
        print("File not found")
        return None

    except json.JSONDecodeError:
        print("File is corrupted or empty")
        return None

    else:
        return favorite_num


favorite_number()


# 10-13 Verify User
FILE_PATH = TEXT_DIR / "username.json"


def greet_user():
    """Greet the user by name."""
    username, is_returning = resolve_username()

    if is_returning:
        print(f"Welcome back, {username}!")
    else:
        print(f"We'll remember you when you come back, {username}!")


def resolve_username():
    username = get_stored_username()

    if username:
        user_answer = input(f"Is your name {username}? (y/n) ")

        if user_answer.lower() == "y":
            return username, True

    return get_new_user(), False


def get_stored_username():
    """Get stored username if available."""
    try:
        with open(FILE_PATH) as f:
            username = json.load(f)

    except FileNotFoundError:
        return None

    else:
        return username


def get_new_user():
    """Prompt for a new username."""
    username = input("What is your name? ")

    with open(FILE_PATH, "w") as f:
        json.dump(username, f)

    return username


greet_user()
