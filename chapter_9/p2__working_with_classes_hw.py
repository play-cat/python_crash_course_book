# task 9-4 Number of customers


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.name} restaurant is currently open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


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


# task 9-5 Login attempts
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nAbout the user {self.first_name}:")
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

    def greet_user(self):
        print(f"\nWelcome, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


person = User("Alex", "Foxman", "afox@mail.com", age=35)
person.greet_user()
person.describe_user()

person.increment_login_attempts()
person.increment_login_attempts()
person.increment_login_attempts()
print(f"{person.first_name} has made {person.login_attempts} attempts to log in.")

person.reset_login_attempts()
print(f"{person.first_name} has made {person.login_attempts} attempts to log in.")
