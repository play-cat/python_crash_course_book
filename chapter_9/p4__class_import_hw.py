from restaurant import Restaurant
from user import Admin

# task 9-10 imported restaurant
new_restaurant = Restaurant("EatDrink", "Ukrainian")

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
print(f"Number of restaurant customers: {new_restaurant.number_served}")

new_restaurant.number_served = 18
print(f"Number of restaurant customers: {new_restaurant.number_served}")

new_restaurant.set_number_served(20)
print(f"Number of restaurant customers: {new_restaurant.number_served}")

new_restaurant.increment_number_served(6)
print(f"Number of restaurant customers: {new_restaurant.number_served}")

# task 9-11 imported Admin
user_1 = Admin("alex", "goodman", "aman@mail.com", 30)
user_1.increment_login_attempts()
user_1.describe_user()
user_1.privileges.show_privileges()
