# import the entire module
# import сar
# my_beetle = car.Car('volkswagen', 'beetle', 2019)

# importing all classes from a module (not recommended)
# from car import *

# importing a single class
# from car import Car

# importing a module into another module
# from car import Car
# from electric_car import ElectricCar

# use of aliases
# from electric_car import ElectricCar as EC
# my_tesla = EC("tesla", "model 3", 2022)

# importing many classes from one module
from car import Car, ElectricCar

car_0 = Car("audi", "a4", 2019)
print(car_0.get_info())
car_0.update_odometer(123)
car_0.read_odometer()

electric_car_0 = ElectricCar("tesla", "model 3", 2022, 62)
print(electric_car_0.get_info())
print(electric_car_0.battery.describe_battery())
print(electric_car_0.battery.get_range())
