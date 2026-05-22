from settings import TEXT_DIR

# from pathlib import Path
## BASE_DIR = Path(__file__).resolve().parent
# TEXT_DIR = BASE_DIR / "text_files"

# try:
#     dangerous_operation()
# except SpecificError:
#     handle_error()
# else:
#     success_logic()
# finally:
#     cleanup()


# Поширені типи винятків
# | Помилка | Коли виникає |
# | `ValueError` | неправильне значення |
# | `TypeError` | неправильний тип |
# | `ZeroDivisionError` | ділення на нуль |
# | `IndexError` | неправильний індекс списку |
# | `KeyError` | ключ відсутній у словнику |
# | `FileNotFoundError` | файл не знайдено |

# Handling the ZeroDivisionError Exception
# print(5 / 0)

# Using try-except Blocks
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Using Exceptions to Prevent Crashes
# Using try-except-else Blocks
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num.lower() == "q":
        break

    second_num = input("Second number: ")
    if first_num.lower() == "q":
        break

    try:
        answer = int(first_num) / int(second_num)

    except ValueError as error:
        print("=" * 16)
        print(error)
        print("Please enter a number.")

    except ZeroDivisionError as error:
        print("=" * 16)
        print(error)
        print("You can't divide by 0!")

    else:
        print("=" * 16)
        print(answer)

# Handling the FileNotFoundError Exception
# Analyzing Text
filename = "alice.txt"
file_path = TEXT_DIR / filename

try:
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")

else:
    # Count the approximate number of words in the file.
    num_words = len(content.split())
    print(f"The file '{filename}' has about {num_words} words.")


# Working with Multiple Files
def get_file_path(filename):
    return TEXT_DIR / filename


def count_words(file_path):
    """Count the approximate number of words in the file."""
    filename = str(file_path).split(sep="\\")[-1]

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

    except FileNotFoundError:
        # Failing Silently
        # No error message is displayed,
        # but the program does not crash either.
        # For this behavior, use the pass operator.
        # pass
        print(f"The file '{filename}' does not exist.")

        with open(TEXT_DIR / "missing_files.txt", "a") as f:
            f.write(f"{filename}\n")

    else:
        num_words = len(content.split())
        print(f"The file '{filename}' has about {num_words} words.")


file_path = get_file_path("alice1.txt")
count_words(file_path)

filenames = [
    "alice.txt",
    "not_file.txt",
    "little_women.txt",
    "moby_dick.txt",
    "siddhartha.txt",
]

for filename in filenames:
    file_path = get_file_path(filename)
    count_words(file_path)
