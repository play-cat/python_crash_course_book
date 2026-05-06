# task 4-3
for i in range(1, 21):
    print(i)

# task 4-4
million_list = list(range(1, 1_000_001))
# for i in million_list:
#     print(i)

# task 4-5
print(min(million_list))
print(max(million_list))
print(sum(million_list))

# task 4-6
even_digits = list(range(1, 21, 2))
for digit in even_digits:
    print(digit)

# task 4-7
threes = list(range(3, 31, 3))
for digit in threes:
    print(digit)

# task 4-8
cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)

for cub in cubes:
    print(cub)

# task 4-9
cubes = [i ** 3 for i in range(1, 11)]
print(cubes)