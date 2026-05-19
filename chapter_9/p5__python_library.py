# Python standard library
from random import randint, choice

print(randint(1, 10))

players = ["charles", "martina", "michael", "gabriel", "eli"]
first_up = choice(players)
print(first_up)
