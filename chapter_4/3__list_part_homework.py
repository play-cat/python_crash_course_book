# task 4-10
from enum import unique

fruits = ['apple','banana','orange','grapes','pineapple','strawberry','watermelon']

print("The first three item in the list are:")
for item in fruits[:3]:
    print(item.title())

print("Three items from the middle of the list are:")
mid_index = len(fruits) // 2
for item in fruits[mid_index - 1:mid_index + 2]:
    print(item.title())

print("Three items from the end of the list are:")
for item in fruits[-3:]:
    print(item.title())

# task 4-11
pizza_list = ['Margherita Pizza', 'Pepperoni Pizza', 'Hawaiian Pizza', 'Four Cheese Pizza', 'Vegetarian Pizza']
friends_pizzas = pizza_list[:]

pizza_list.append('Noname Pizza')
friends_pizzas.append('Unnamed Pizza')

print('My favourite pizzas are:')
for pizza in pizza_list:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)

# task 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

all_foods = list(set(my_foods + friend_foods))
for food in all_foods:
    print(food)


