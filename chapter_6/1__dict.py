# Simple dict
alien_0 = {
    "color": "green",
    "points": 5,
}

print(alien_0["color"])
print(alien_0["points"])

# Звернення до словника
new_points = alien_0["points"]
print(f"You just earned {new_points} points.")

# Додавання пар ключ:значення
alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

# Empty dict
my_dict = {}

my_dict["simple_key"] = "simple_value"

print(my_dict)

# Edit dict value
alien_0 = {"color": "green"}
print(f"The alien is {alien_0['color']}")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}")

alien_0 = {
    "x_position": 0,
    "y_position": 25,
    "speed": "medium",
}
print(f"Alien original x-position: {alien_0['x_position']}")

# Зсунути прибульця праворуч
# Визначити, як далеко зсунути прибульця
# зважаючи на його поточну швидкість
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
elif alien_0["speed"] == "fast":
    x_increment = 3

# Нове розташування, це попереднє розташування + зміщення
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"Alien new x-position is {alien_0['x_position']}")

# Delete key:value
alien_0 = {
    "color": "green",
    "points": 5,
}

del alien_0["points"]
print(alien_0)

# Совник схожих об'єктів
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "alex": "python",
}

language = favorite_languages["alex"].title()
print(f"Alex's favorite language is {language}.")

# Звернення до значень списку за допомогою .get()
alien_0 = {
    "color": "green",
    "speed": "slow",
}

point_value = alien_0.get("points", "No point value assigned.")
print(f"You earned points: {point_value}")
