# task 3-4
names = ['Alex', 'David', 'Carol']

print(f"Hi, {names[0]} I'd like to invite you to dinner.")
print(f"Hi, {names[1]} I'd like to invite you to dinner.")
print(f"Hi, {names[2]} I'd like to invite you to dinner.")

# task 3-5
print(f"{names[1]} can't come.")
names[1] = 'John'

print(f"Hi, {names[0]} I'd like to invite you to dinner.")
print(f"Hi, {names[1]} I'd like to invite you to dinner.")
print(f"Hi, {names[2]} I'd like to invite you to dinner.")

# task 3-6
print(f'Hey, {names[0]}, {names[1]}, {names[2]}! I bought a new dining table, so now I can invite more guests.')
names.insert(0, 'Jane')
names.insert(2, 'Mary')
names.append('Mike')

print(f"Hi, {names[0]} I'd like to invite you to dinner.")
print(f"Hi, {names[1]} I'd like to invite you to dinner.")
print(f"Hi, {names[2]} I'd like to invite you to dinner.")
print(f"Hi, {names[3]} I'd like to invite you to dinner.")
print(f"Hi, {names[4]} I'd like to invite you to dinner.")
print(f"Hi, {names[5]} I'd like to invite you to dinner.")

# task 3-7
print("Hi all, I'm sorry, but I can only invite two guests.")

print(f"I'm sorry, {names.pop()}, but I can only invite two guests.")
print(f"I'm sorry, {names.pop()}, but I can only invite two guests.")
print(f"I'm sorry, {names.pop()}, but I can only invite two guests.")
print(f"I'm sorry, {names.pop()}, but I can only invite two guests.")

print(f"Hello, {names[0]}, I’ll be happy to see you at dinner.")
print(f"Hello, {names[1]}, I’ll be happy to see you at dinner.")

del names[0]
del names[0]

print(names)

