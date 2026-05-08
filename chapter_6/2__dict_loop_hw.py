# task 6-4 Glossary 2
terms_glossary = {
    "list": "Впорядкована змінна колекція елементів, що може містити різні типи даних. Створюється за допомогою квадратних дужок [].",
    "tuple": "Впорядкована, але незмінна колекція елементів. Створюється за допомогою круглих дужок ().",
    "dict": "Структура даних у форматі ключ:значення, де кожен ключ унікальний. Створюється за допомогою фігурних дужок {}.",
    "set": "Невпорядкована колекція унікальних елементів. Використовується для операцій над множинами (перетин, об’єднання тощо).",
    "function": "Блок коду, який можна викликати багаторазово. Оголошується за допомогою ключового слова def.",
}

print("Python glossary of terms")
for term, definition in terms_glossary.items():
    print(f"{term}:\n\t{definition}")

# task 6-5 Rivers
rivers = {
    "nile": "egypt",
    "dnipro": "ukraine",
    "euphrates": "turkey",
}

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

# task 6-6 Pool
pool_list = ["jen", "andrew", "marry", "sarah", "jane", "edward", "phil", "alex"]

favorite_languages = {
    "jen": "python",
    "andrew": "java script",
    "sarah": "c",
    "edward": "ruby",
    "alex": "python",
}

for person in sorted(pool_list):
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for taking the pool!")
    else:
        print(f"{person.title()}, please take our pool!")

# другий варіант виконання з list comprehension
respondents = [
    f"{person.title()}, thank you for taking the pool!"
    for person in sorted(pool_list)
    if person in favorite_languages.keys()
]

non_respondents = [
    f"{person.title()}, please take our pool!"
    for person in sorted(pool_list)
    if person not in favorite_languages.keys()
]

print("\n".join(respondents))
print("\n".join(non_respondents))
