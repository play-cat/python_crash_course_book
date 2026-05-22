import re

from settings import TEXT_DIR

# task 10-6 Addition

number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")

try:
    print(f"Sum of given numbers: {int(number_1) + int(number_2)}")

except ValueError:
    print("Please enter numbers only.")

# task 10-7 Addition Calculator
print("Give me two numbers, and I'll add them together.")
print("Enter 'q' to quit.")

while True:
    number_1 = input("Enter the first number: ")
    if number_1 == "q":
        break

    number_2 = input("Enter the second number: ")
    if number_2 == "q":
        break

    try:
        result = int(number_1) + int(number_2)

    except ValueError:
        print("=" * 16)
        print("Please enter numbers only.\n")

    else:
        print("=" * 16)
        print(f"Sum of given numbers: {result}\n")

# task 10-8 Cats and Dogs
file_list = ["missing_file.txt", "cats.txt", "dogs.txt"]


def get_file_path(filename):
    return TEXT_DIR / filename


def print_file(filename):
    try:
        file_path = get_file_path(filename)
        with open(file_path, encoding="utf-8") as f:
            print(f"Contents of the file: '{filename}'")
            print(f.read())

    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        # task 10-9. Silent Cats and Dogs
        # pass


for f in file_list:
    print_file(f)

# task 10-10 Common Words
file_list = [
    "alice.txt",
    "not_file.txt",
    "little_women.txt",
    "moby_dick.txt",
    "missing_file.txt",
    "siddhartha.txt",
]


def count_word_occurrences(content, word):
    pattern = rf"\b{re.escape(word)}\b"
    matches = re.findall(pattern, content, re.IGNORECASE)
    # matches_alt = re.finditer(pattern, content, re.IGNORECASE)
    # return sum(1 for _ in matches_alt)
    return len(matches)


def common_words_count(filename, word):

    try:
        file_path = get_file_path(filename)
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

    except FileNotFoundError as error:
        print(f"{error}\nThe file '{filename}' does not exist.")
        return 0

    return count_word_occurrences(content, word)


result = common_words_count("alice.txt", "the")
print(result)
