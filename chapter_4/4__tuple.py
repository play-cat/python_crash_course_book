# Tuple - Кортеж
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

my_tuple = (3,) # має бути хоч одна кома, інакше це буде просто число, а не кортеж
print(type(my_tuple))

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)