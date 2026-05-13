# task 8-12 sandwich
def make_sandwich(*ingredients):
    print("\nThe following ingredients will be added to the sandwich:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


sandwich_ingredients_1 = [
    "Lettuce",
    "Tomato",
    "Cheddar Cheese",
    "Onion",
    "Bacon",
    "Mayonnaise",
]
sandwich_ingredients_2 = [
    "Tomato",
    "Pickles",
    "Bacon",
    "Grilled Chicken",
    "Mayonnaise",
]
sandwich_ingredients_3 = [
    "Lettuce",
    "Tomato",
    "Cheddar Cheese",
    "Onion",
    "Beef Patty",
    "Mayonnaise",
]
make_sandwich(*sandwich_ingredients_1)
make_sandwich(*sandwich_ingredients_2)
make_sandwich(*sandwich_ingredients_3)


# task 8-13 user profile
def build_profile(first, last, **user_data):
    user_data["first_name"] = first
    user_data["last_name"] = last
    return user_data


user_profile = build_profile("alex", "korev", location="seattle", occupation="surgeon")
print(f"\nUser data: {user_profile}")

for key, value in user_profile.items():
    print(f"{key}: {value.title()}")


# task 8-14 cars
def make_car(brand, model, **car_data):
    car = {
        "brand": brand,
        "model": model,
    }
    car.update(car_data)
    return car


my_car_1 = make_car("bmw", "X5", color="black", tow_package=True)
print(f"\nCar info: {my_car_1}")

my_car_2 = make_car("skoda", "kodiaq", color="silver", tow_package=False)
print(f"\nCar info: {my_car_2}")
