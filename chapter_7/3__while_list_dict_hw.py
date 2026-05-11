# task 7-8 Cafe
sandwich_orders = [
    "Club Sandwich",
    "BLT Sandwich",
    "Grilled Cheese Sandwich",
    "Turkey and Avocado Sandwich",
    "Ham and Cheese Sandwich",
]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich.title()}")

print("Prepared sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

# task 7-9 The pastrami is over.
sandwich_orders = [
    "Club Sandwich",
    "Pastrami sandwich",
    "BLT Sandwich",
    "Grilled Cheese Sandwich",
    "Pastrami sandwich",
    "Turkey and Avocado Sandwich",
    "Ham and Cheese Sandwich",
    "Pastrami sandwich",
]
finished_sandwiches = []

print("\nSorry, the cafe is out of pastrami.")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich.title()}")

print("\nPrepared sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

# task 7-10 Perfect vacation
responses = {}
poll_active = True

while poll_active:
    name = input("\nWhat is your name? ")
    response = input("Where do you want to go on vacation this summer? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        poll_active = False

print("\n----- Pool results -----")
for name, response in responses.items():
    print(f"{name.title()} wants to go on vacation to the {response.title()}")
