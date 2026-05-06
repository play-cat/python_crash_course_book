# if conditional_test:
#     do something
age = 19

if age >= 18:
    print(f"You are old enough to vote!")
    print(f"Have you registered to vote yet?")

# if-else
age = 17

if age >= 18:
    print(f"You are old enough to vote!")
    print(f"Have you registered to vote yet?")
else:
    print(f"Sorry, you are too young to vote!")
    print(f"Please register to vote as soon as you turn 18!")

# if-elif-else
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"You admission cost is ${price}.")

# Тернарний вираз
price = 0 if age < 4 else \
        25 if age < 18 else \
        40
# price = 0 if age < 4 else 25 if age < 18 else 40

print(f"You admission cost is ${price}.")

# кілька блоків elif
age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"You admission cost is ${price}.")

# Пропуск блоку else
age = 43
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"You admission cost is ${price}.")

# Перевірка декількох умов
request_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in request_toppings:
    print("Adding mushrooms.")
if 'extra cheese' in request_toppings:
    print("Adding extra cheese.")
if 'pepperoni' in request_toppings:
    print("Adding pepperoni.")

print("\nFinished making you pizza!")
