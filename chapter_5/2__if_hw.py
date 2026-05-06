# task 5-3
user_points = 0
alien_color = 'green'

if alien_color == 'green':
    user_points += 5
    print('+5 points received!')
    print(f'Total points: {user_points}')
if alien_color == 'red':
    user_points += 15
    print('+15 points received!')
    print(f'Total points: {user_points}')

# task 5-4
user_points = 0
alien_color = 'yellow'

if alien_color == 'green':
    user_points += 5
    print('+5 points received!')
    print(f'Total points: {user_points}')
else:
    user_points += 10
    print('+10 points received!')
    print(f'Total points: {user_points}')

# task 5-5
user_points = 0
alien_color = 'red'

if alien_color == 'green':
    user_points += 5
    print('+5 points received!')
    print(f'Total points: {user_points}')
elif alien_color == 'yellow':
    user_points += 10
    print('+10 points received!')
    print(f'Total points: {user_points}')
elif alien_color == 'red':
    user_points += 15
    print('+15 points received!')
    print(f'Total points: {user_points}')

# task 5-6
age = 43

if age < 2:
    print('infant')
elif age < 5:
    print('toddler')
elif age < 13:
    print('child')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adult')
else:
    print('elderly')

# task 5-7
favourite_fruits = ['apple', 'banana', 'orange']

if 'apple' in favourite_fruits:
    print('You really like apple!')
if 'banana' in favourite_fruits:
    print('You really like banana!')
if 'orange' in favourite_fruits:
    print('You really like orange!')
if 'pineapple' in favourite_fruits:
    print('You really like pineapple!')
if 'watermelon' in favourite_fruits:
    print('You really like watermelon!')