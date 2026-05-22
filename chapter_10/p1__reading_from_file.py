# Reading the entire file

with open("pi_digits.txt", mode="r", encoding="utf-8") as file:
    contents = file.read()
    print(contents)
    # print(contents.strip())

# file paths
# relative path to the file
with open("text_files/simple_text_file.txt") as file2:
    content2 = file2.read()
print(content2)

# absolute path to the file
file_path = "../chapter_10/text_files/simple_text_file.txt"
with open(file_path) as file3:
    content3 = file3.read()
print(content3)

# line-by-line reading
filename = "pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# creating a list of lines based on a file
with open(filename) as file_object:
    file_lines = file_object.readlines()

print(file_lines)

for line in file_lines:
    print(line.rstrip())

# working with file's contents
with open(filename) as file:
    file_lines = file.readlines()

pi_string = ""
for line in file_lines:
    pi_string += line.strip()

print(f"\n{pi_string}")
print(len(pi_string))

# big files: one million digits
filename = "pi_million_digits.txt"

with open(filename) as file:
    lines = file.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:82]}...")
print(len(pi_string))


# is your birthday contained in PI?
def is_your_birthday_in_pi(birthdate):
    if birthdate and len(birthdate) == 6:
        if birthdate in pi_string:
            print(f"You birthdate appears in thr first million digits of pi!")
        else:
            print("You birthdate does not appears in thr first million digits of pi.")
    else:
        print("Date of birth must consist of 6 digits.")


birthday = input("\nEnter your birthdate, in the form ddmmyy: ")
is_your_birthday_in_pi(birthday)
