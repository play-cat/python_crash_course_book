# task 6-7 People
person_1 = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 21,
    "city": "New York",
}
person_2 = {
    "first_name": "Marie",
    "last_name": "Bond",
    "age": 19,
    "city": "Paris",
}
person_3 = {
    "first_name": "Bob",
    "last_name": "Smith",
    "age": 34,
    "city": "Dallas",
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"\nFirst_name: {person.get('first_name')}")
    print(f"Last_name: {person.get('last_name')}")
    print(f"Age: {person.get('age')}")
    print(f"Live in: {person.get('city')}")

# task 6-8 Pets
pet_1 = {
    "species": "cat",
    "name": "Bob",
    "owner": "Bill",
}
pet_2 = {
    "species": "dog",
    "name": "Phoebe",
    "owner": "Carol",
}

pets = [pet_1, pet_2]

for pet in pets:
    print(
        f"\n{pet.get('name')} is a {pet.get('species')}, whose owner is {pet.get('owner')}."
    )
