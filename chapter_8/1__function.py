def greet_user(username):
    """Shows a simple greeting"""
    print(f"Welcome to Chapter 8, {username.title()}!")


print(greet_user.__doc__)
greet_user("Alex")
