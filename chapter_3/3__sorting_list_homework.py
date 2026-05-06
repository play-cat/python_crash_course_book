# task 3-8
from asyncio import tasks

cities = ['New York', 'Paris', 'London', 'Tokyo', 'Oslo']
print(cities)

print(sorted(cities))
print(cities)

print(sorted(cities, reverse=True))
print(cities)

cities.reverse()
print(cities)

cities.reverse()
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

# task 3-9
print(f"Number of cities: {len(cities)}.")

# task 3-10
fruits = ['banana', 'apple', 'orange', 'lemon']
print(fruits)

print(sorted(fruits, reverse=True))

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

print(len(fruits))

