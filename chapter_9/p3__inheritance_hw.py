from car import Car
from p2__working_with_classes_hw import Restaurant
from p2__working_with_classes_hw import User

# from p3__inheritance import Car
# from p3__inheritance import ElectricCar


# task 9-6 ice cream stand
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, *flavors):
        super().__init__(name, cuisine_type)
        self.flavors = {flavor.lower() for flavor in flavors}

    def show_flavors(self):
        if self.flavors:
            print("Available ice cream flavors:")
            for flavor in sorted(self.flavors):
                print(f"- {flavor.title()}")
        else:
            print("The menu is empty.")

    def add_flavors(self, *flavors):
        for flavor in flavors:
            normalized = flavor.lower()
            if normalized not in self.flavors:
                self.flavors.add(normalized)
                print(f"{flavor.title()} added to the list of flavors.")
            else:
                print(f"{flavor.title()} already in the list of flavors.")

    def remove_flavors(self, *flavors):
        for flavor in flavors:
            normalized = flavor.lower()
            if normalized in self.flavors:
                self.flavors.remove(normalized)
                print(f"{flavor.title()} removed from the list of flavors.")
            else:
                print(f"{flavor.title()} not in the list of flavors.")


today_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip",
    "Cookies and Cream",
]
ice_cream_stand_0 = IceCreamStand("Best Ice Cream", "Ukrainian", *today_flavors)
print(ice_cream_stand_0.describe_restaurant())
ice_cream_stand_0.show_flavors()
ice_cream_stand_0.add_flavors("cream brule", "blueberry")
ice_cream_stand_0.remove_flavors("strawberry")


# task 9-7 admin
class Admin(User):
    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = {"can add post", "can delete post", "can ban user"}

    def show_privileges(self):
        if self.privileges:
            print("\nThis user has the following administrator privileges:")
            for privilege in self.privileges:
                print(f"- {privilege.title()}")


user_0 = Admin("alex", "goodman", "aman@mail.com", 29)
user_0.describe_user()
user_0.show_privileges()


# task 9-8 privileges
class Privileges:
    DEFAULT_PRIVILEGES = {
        "add_post": "can add post",
        "delete_post": "can delete post",
        "ban_user": "can ban user",
    }

    def __init__(self):
        self.privileges = self.DEFAULT_PRIVILEGES.copy()

    def show_privileges(self):
        if self.privileges:
            print("\nThis user has the following administrator privileges:")
            for value in self.privileges.values():
                print(f"- {value.title()}")


class Admin(User):
    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = Privileges()


user_1 = Admin("alex", "goodman", "aman@mail.com", 30)
user_1.increment_login_attempts()
user_1.describe_user()
user_1.privileges.show_privileges()


# task 9-9 upgrade battery
class Battery:
    DEFAULT_BATTERY_SIZE = 75
    RANGE_BY_SIZE = {
        75: 440,
        100: 600,
    }

    def __init__(self, battery_size=None):
        if battery_size is None:
            battery_size = self.DEFAULT_BATTERY_SIZE
        self.battery_size = battery_size

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print("The car battery has been upgraded to 100-kWh.")

    def get_range(self):
        """Return estimated driving range."""
        estimated_range = self.RANGE_BY_SIZE.get(self.battery_size)

        if estimated_range is None:
            estimated_range = self.calculated_custom_range()

        return f"This car can go about {estimated_range} kilometers on a full charge."

    def calculated_custom_range(self, km_by_kwh=5.9):
        return self.battery_size * km_by_kwh


class ElectricCar(Car):
    """Initialize the attributes of the parent class.
    Then initialize the attributes of the electric car."""

    def __init__(self, make, model, year, battery_size=None):
        super().__init__(make, model, year)
        # defining attributes of the derived class
        self.battery = Battery(battery_size)


electric_car_3 = ElectricCar("tesla", "model y", 2021, 120)
print(electric_car_3.get_info())
print(electric_car_3.battery.describe_battery())
print(electric_car_3.battery.get_range())

electric_car_4 = ElectricCar("tesla", "model 3", 2022, 62)
print(electric_car_4.get_info())
print(electric_car_4.battery.describe_battery())
print(electric_car_4.battery.get_range())

electric_car_4.battery.upgrade_battery()
print(electric_car_4.battery.describe_battery())
print(electric_car_4.battery.get_range())
