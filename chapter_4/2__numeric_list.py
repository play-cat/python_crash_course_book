# range()
for value in range(1, 5):
    print(value)

for value in range(5):
    print(value)

# list()
numbers = list(range(6))
print(numbers)

# even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# squares
squares = []

for i in range(1, 11):
    squares.append(i ** 2)

print(squares)

# min, max, sum
digits = list(range(10))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squares)