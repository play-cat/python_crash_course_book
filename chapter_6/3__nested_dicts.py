# list of dictionaries
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# empty list for generated aliens
aliens = []

# Create 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# first 5 aliens
for alien in aliens[:5]:
    print(alien)

print("...")

# Show how many aliens have been created
print(f"Total numbers of aliens: {len(aliens)}")

# Change first 3 aliens
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

for alien in aliens[:5]:
    print(alien)

# list in the dictionary
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print("\t" + topping)

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

for name, langs in favorite_languages.items():
    if len(langs) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for lang in langs:
            print(f"\t{lang.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        print(f"\t{langs[0].title()}")

# dictionary in the dictionary
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]

    print(f"\nUsername: {username.title()}")
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
