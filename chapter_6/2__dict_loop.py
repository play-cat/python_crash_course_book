# Перебрати усі пари ключ:значення
user_0 = {
    "username": "efermi",
    "fist": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    "jen": "python",
    "andrew": "java script",
    "sarah": "c",
    "edward": "ruby",
    "alex": "python",
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is: {language.title()}.")

# Перебрати всі ключі у словнику
for name in favorite_languages.keys():
    print(name.title())

# за замовчуванням якщо не вказати метод словника,
# то буде використовуватись .keys()
# тому можна писати так:
# for name in favorite_languages:
#     print(name.title())

friends = ["alex", "andrew"]

for name in favorite_languages:
    print(f"Hi, {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our pool!")

# Як перебрати усі ключі в словнику в певній послідовності
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the pool!")

# Як перебрати всі значення у словнику
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Як перебрати унікальні значення у словнику
# set - множина, що зберігає лише унікальні елементи. Всі дублі видаляються
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
