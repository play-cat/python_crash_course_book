# list slice
players = ['charles', 'martin', 'michael', 'ghoul', 'eli']
print(players)
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-2:]) # last 2 items
print(players[::2]) # steps

# brake and loops
print('Here are the first three players:')
for player in players[:3]:
    print(player.title())

# copy list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('My favourite foods are:')
print(my_foods)

print('My friend\'s favourite foods are:')
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favourite foods are:')
print(my_foods)
print('My friend\'s favourite foods are:')
print(friend_foods)

