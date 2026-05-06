# sort()
# Sort the list in ascending order and return None.
# The sort is in-place (i.e. the list itself is modified)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

 # sorted()
# Return a new list containing all items from the iterable in ascending order.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Original list:')
print(cars)

print('Sorted list:')
print(sorted(cars))

print('Original list again:')
print(cars)

# reverse() reversed list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# len() Return the number of items in a container.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
