# task 9-1 Restaurant
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} restaurant is currently open.")


new_restaurant = Restaurant("EatDrink", "Ukrainian")

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

# task 9-2
new_restaurant_1 = Restaurant("Meat and sausage", "Italian")
new_restaurant_2 = Restaurant("Hot Peper", "Mexican")

new_restaurant_1.describe_restaurant()
new_restaurant_2.describe_restaurant()


# task 9-3 User
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def describe_user(self):
        print(f"\nAbout the user {self.first_name}:")
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

    def greet_user(self):
        print(f"\nWelcome, {self.first_name} {self.last_name}!")


person = User("Alex", "Foxman", "afox@mail.com", age=35)
person.greet_user()
person.describe_user()
