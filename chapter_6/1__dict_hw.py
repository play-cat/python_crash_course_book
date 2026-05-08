# task 6-1 Person
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 21,
    "city": "New York",
}

print("About the person:")
print(f"First_name: {person['first_name']}")
print(f"Last_name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"Live in the city: {person['city']}")
print(f"Birthday: {person.get('birthday', 'Not available')}")

# task 6-2 Favorite numbers
favorite_numbers = {
    "alice": 10,
    "bob": 20,
    "charlie": 30,
    "alex": 40,
    "john": 50,
}

numbers_sum = (
    favorite_numbers["alice"]
    + favorite_numbers["bob"]
    + favorite_numbers["charlie"]
    + favorite_numbers["alex"]
    + favorite_numbers["john"]
)

print(f"Sum of favorite numbers: {numbers_sum}")

# task 6-3 Glossary
terms_glossary = {
    "list": "Впорядкована змінна колекція елементів, що може містити різні типи даних. Створюється за допомогою квадратних дужок [].",
    "tuple": "Впорядкована, але незмінна колекція елементів. Створюється за допомогою круглих дужок ().",
    "dict": "Структура даних у форматі ключ:значення, де кожен ключ унікальний. Створюється за допомогою фігурних дужок {}.",
    "set": "Невпорядкована колекція унікальних елементів. Використовується для операцій над множинами (перетин, об’єднання тощо). Створюється за допомогою фігурних дужок {}.",
    "function": "Блок коду, який можна викликати багаторазово. Оголошується за допомогою ключового слова def.",
}

print("Python glossary of terms")
print(f"list:\n\t{terms_glossary['list']}")
print(f"tuple:\n\t{terms_glossary['tuple']}")
print(f"dict:\n\t{terms_glossary['dict']}")
print(f"set:\n\t{terms_glossary['set']}")
print(f"function:\n\t{terms_glossary.get('function')}")
