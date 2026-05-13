# Pass any number of arguments to a function *args
def make_pizza(*toppings):
    """Describe the pizza we are going to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


toppings_list = ["pepperoni", "mushrooms", "extra cheese", "green peppers"]
make_pizza(*toppings_list)


# How to combine free and positional arguments
def make_pizza(size, *toppings):
    """Describe the pizza we are going to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


toppings_list = ["pepperoni", "mushrooms", "extra cheese", "green peppers"]
make_pizza(16, *toppings_list)


# Arbitrary keyword arguments **kwargs
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)

print(f"\nUser data: {user_profile}")
