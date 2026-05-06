cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Перевірка на рівність
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

# Перевірка нерівності
request_topping = 'mushrooms'

if request_topping != 'anchovies':
    print('Hold the anchovies')

# Числові порівняння
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print('That is not correct answer. Please try again.')

age =19
print(age > 21)
print(age < 21)
print(age >= 21)
print(age <= 21)

# Перевірка кількох умов
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 23
print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# Перевірка наявності. Чи є значення у списку.
request_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in request_toppings)
print('pepperoni' in request_toppings)

# Перевірка відсутності. Чи відсутнє значення у списку.
banned_users = ['alice', 'david', 'carol']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Булеві вирази
game_active = True
can_edit = False