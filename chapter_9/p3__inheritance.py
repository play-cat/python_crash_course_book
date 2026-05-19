import json


class Car:
    """A simple attempt to model a car"""

    total_cars_produced = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_capacity = 100

        Car.total_cars_produced += 1

    def show_info(self):
        return f"\n{self.year} {self.make} {self.model}".title()

    def read_odometer(self):
        """Displays a message with the car's mileage"""
        print(f"This car has {self.odometer_reading} kilometers on it.")

    def update_odometer(self, kilometers):
        if kilometers >= self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, kilometers):
        if kilometers >= 0:
            self.odometer_reading += kilometers

    def fill_gas_tank(self):
        self.gas_tank_capacity = 100

    @staticmethod
    def get_number_cars_produced():
        print(f"\nTotal number of cars produced: {Car.total_cars_produced}")

    # Альтернативний конструктор з рядка
    @classmethod
    def from_string(cls, car_string):
        # Формат: "Tesla,Model 3,2022"
        make, model, year = car_string.split(",")
        return cls(make, model, int(year))

    # Альтернативний конструктор з JSON
    @classmethod
    def from_json(cls, json_string):
        # Очікуємо json_string '{"make": "...", "model": "...", "year": ...}'
        data = json.loads(json_string)
        return cls(data["make"], data["model"], data["year"])

    # Альтернативний конструктор зі словника
    @classmethod
    def from_dict(cls, data):
        # Очікуємо словник {"make": "...", "model": "...", "year": ...}
        return cls(data["make"], data["model"], data["year"])

    # Альтернативний конструктор з рядка БД
    @classmethod
    def from_db_row(cls, row):
        # Очікуємо кортеж (make, model, year)
        make, model, year = row
        return cls(make, model, year)


# __init__() method of the derived class
class ElectricCar(Car):
    """Initialize the attributes of the parent class.
    Then initialize the attributes of the electric car."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # defining attributes of the derived class
        self.battery_size = 75
        self.gas_tank_capacity = self.fill_gas_tank()

    # defining methods of the derived class
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    # overriding parent class methods
    def fill_gas_tank(self):
        return "This car doesn't need a gas tank!"


car0 = Car("renault", "duster", 2022)
electric_car_0 = ElectricCar("tesla", "model s", 2019)

print(electric_car_0.show_info())
electric_car_0.describe_battery()
print(electric_car_0.gas_tank_capacity)


# instances as attributes
class Battery:
    DEFAULT_BATTERY_SIZE = 75

    RANGE_BY_SIZE = {
        75: 260,
        100: 350,
    }

    def __init__(self, battery_size=None):
        if battery_size is None:
            battery_size = self.DEFAULT_BATTERY_SIZE

        self.battery_size = battery_size

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."

    def get_range(self):
        """Return estimated driving range."""
        estimated_range = self.RANGE_BY_SIZE.get(self.battery_size, 0)

        return f"This car can go about {estimated_range} kilometers on a full charge."


class ElectricCar(Car):
    """Initialize the attributes of the parent class.
    Then initialize the attributes of the electric car."""

    def __init__(self, make, model, year, battery_size=None):
        super().__init__(make, model, year)
        # defining attributes of the derived class
        self.battery = Battery(battery_size)


electric_car_1 = ElectricCar("tesla", "model y", 2020)
print(electric_car_1.show_info())
print(electric_car_1.battery.describe_battery())
print(electric_car_1.battery.get_range())
