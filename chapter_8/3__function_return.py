# return
def get_formated_name(first_name, last_name):
    """Returns the formatted full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formated_name("jimi", "hendrix")
print(musician)


# optional argument
def get_formated_name(first_name, last_name, middle_name=None):
    """Returns the formatted full name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formated_name("jimi", "hendrix")
print(musician)
musician = get_formated_name("john", "hooker", "lee")
print(musician)


# dictionary return
def build_person(first_name, last_name, age=None):
    """Returns a person instance"""
    person = {
        "first_name": first_name,
        "last_name": last_name,
    }
    if age:
        person["age"] = age

    return person


person = build_person("jimi", "hendrix")
print(person)
person = build_person("jimi", "hendrix", 40)
print(person)

# func and while loop
while True:
    print("\nPlease tell me your name:")
    print('(enter "q" at any time to quit)')

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formated_name = get_formated_name(f_name, l_name)
    print(f"\nHello, {formated_name.title()}!")
