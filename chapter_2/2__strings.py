name = "Ada miller"
print(name)
print(name.title())
print(name.upper())
print(name.lower())

# f string
first_name = "adam"
last_name = "sendler"
# full_name = first_name + " " + last_name
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# space symbols
print("\tPython") #tab
print("Languages:\nPython\nC++\nJavaScript") #new line
print("Languages:\n\tPython\n\tC++\n\tJavaScript") #new line + tab

# strip() rstrip() lstrip()
favorite_language = " python "
favorite_language = favorite_language.strip()
print(favorite_language)

# apostrophe
message = "One of Python's strengths is its diverse community."
print(message)