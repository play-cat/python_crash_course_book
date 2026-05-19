# Creating and using a Сlass
# Create Class Dog
class Dog:
    """Just an attempt to simulate a dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Seat simulation"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """rollover simulation"""
        print(f"{self.name} is now rolling over.")

    def bark(self, amount=1):
        """bark simulation"""
        print(f"{self.name} is now barking: " + "bark! " * amount)

    def birthday(self):
        """age+1"""
        self.age += 1
        print(f"{self.name} is now birthday!")
        print(f"{my_dog.name} is {my_dog.age} years old.")


# Creating an instance of a class
my_dog = Dog("Phoebe", 6)

# Accessing attributes
print(f"My dog's name is {my_dog.name}.")
print(f"{my_dog.name} is {my_dog.age} years old.")

# Calling methods
my_dog.sit()
my_dog.roll_over()
my_dog.bark(3)
my_dog.birthday()
