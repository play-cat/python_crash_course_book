motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change a list item
motorcycles[0] = 'ducati'
print(motorcycles)

# add new list element
motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# insert new list element
motorcycles.insert(0, 'ducati')
print(motorcycles)

# delete list element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# del
del motorcycles[1]
print(motorcycles)

# pop() - Remove and return item at index (default last)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# remove() Removing a list item by value. Remove first occurrence of value.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")
