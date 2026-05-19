import json

"""A set of classes for modeling gasoline and electric cars"""


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

    def get_info(self):
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


class ElectricCar(Car):
    """Initialize the attributes of the parent class.
    Then initialize the attributes of the electric car."""

    def __init__(self, make, model, year, battery_size=None):
        super().__init__(make, model, year)
        # defining attributes of the derived class
        self.battery = Battery(battery_size)


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
