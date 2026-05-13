# Позиційні аргументи
def describe_pet(animal_type, pet_name):
    """Показує інформацію про домашнього улюбленця"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("cat", "sofa")
describe_pet("dog", "phoebe")

# Ключові аргументи
describe_pet(pet_name="willie", animal_type="hamster")


# Default value
def describe_pet(pet_name, animal_type="dog"):
    """Показує інформацію про домашнього улюбленця"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("phoebe")
describe_pet("phoebe", "cat")
