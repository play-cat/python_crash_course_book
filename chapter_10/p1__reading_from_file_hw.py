# task 10-1 learning python
filename = "learning_python.txt"

with open(filename) as f:
    content = f.read()
    print(content)

print("")

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("")

with open(filename) as f:
    content = f.readlines()
for line in content:
    print(line.rstrip())


# task 10-2 learning Java Script
def replace_word(file_path, search, replace):
    with open(file_path) as file:
        # return [line.replace(search, replace) for line in file]
        text = file.read()
    return text.replace(search, replace)


replaced_text = replace_word(filename, "Python", "Java Script")
print()
# for l in replaced_text:
#     print(l.rstrip())
print(replaced_text)
