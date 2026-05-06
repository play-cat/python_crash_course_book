# Моніторинг особливих елементів списку
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
unavailable_toppings = ['green peppers']

for topping in requested_toppings:
    if topping in unavailable_toppings:
        print(f"Sorry, we are uot of {topping} right now.")
    else:
        print(f"Adding {topping}.")

print("\nFinished making your pizza!")

# Перевірка, чи список не порожній
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Використання кількох списків
available_toppings = ['mushrooms', 'green peppers', 'extra cheese',
                        'olives', 'pepperoni', 'pineapple']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if requested_toppings:
    for topping in requested_toppings:
        if topping in available_toppings:
            print(f"Adding {topping}.")
        else:
            print(f"Sorry, we don't have {topping}.")

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


