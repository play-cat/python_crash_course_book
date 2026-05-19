import json


class Car:
    """A simple attempt to model a car"""

    total_cars_produced = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

        Car.total_cars_produced += 1

    def get_info(self):
        return f"{self.year} {self.make} {self.model}".title()

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

    @staticmethod
    def get_number_cars_produced():
        print(f"\nTotal number of cars produced: {Car.total_cars_produced}")


# Імітуємо результат SQL-запиту
db_row = ("Toyota", "Corolla", 2019)


# Використання
car0 = Car("renault", "duster", 2022)
car1 = Car.from_string("Audi,A4,2020")
car2 = Car.from_json('{"make": "BMW", "model": "X5", "year": 2021}')
car3 = Car.from_dict({"make": "Tesla", "model": "Model 3", "year": 2022})
car4 = Car.from_db_row(db_row)

print(car0.get_info())
print(car1.get_info())  # 2020 Audi A4
print(car2.get_info())  # 2021 BMW X5
print(car3.get_info())  # 2022 Tesla Model 3
print(car4.get_info())  # 2019 Toyota Corolla

car0.read_odometer()

Car.get_number_cars_produced()

# Changing the attribute value

# Directly changing the value
car0.odometer_reading = 35
car0.read_odometer()

# Changing the value in a method
# See update_odometer() method
car0.update_odometer(32_210)
car0.read_odometer()

# Incrementing an attribute in a method
# See increment_odometer() method
car0.increment_odometer(350)
car0.read_odometer()
