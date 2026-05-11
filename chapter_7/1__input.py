# input()
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("What is your name? ")
print(f"Hello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is you first name? "

name = input(prompt)
print(f"Hello, {name}!")

# int() and input()
age = input("How old are you? ")
age = int(age)
print(age >= 18)

height = int(input("How tall are you, in inches? "))

if height >= 48:
    print(f"\nYou're tall enough to ride.")
else:
    print(f"\nYou'll be able to ride when you're a little older.")

# Оператори остачі
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

number = int(input("Enter a number, and I'll tell you it it's even or odd: "))

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
