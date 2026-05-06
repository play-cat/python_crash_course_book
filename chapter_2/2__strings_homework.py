# task 2-3
from chapter_2.strings import full_name

name = "Eric Master"
print(f"Hello, {name}, how are you?!")

# task 2-4
print(name.upper())
print(name.lower())
print(name.title())

# task 2-5
print(f'\tАльберт Енштейн якось сказав: "Хто ніколи не помилявся,\n\tтой ніколи не брався за щось нове".')

# task 2-6
famous_person = "Альберт Енштейн"
message = f'\t{famous_person} якось сказав: "Хто ніколи не помилявся,\n\tтой ніколи не брався за щось нове".'
print(message)

# task 2-7
full_name = "\tJohn Dou "
print(full_name)
print(full_name.lstrip())
print(full_name.rstrip())
print(full_name.strip())