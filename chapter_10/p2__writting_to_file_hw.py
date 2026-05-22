# task 10-3 Guest
filename = "guest.txt"
name = input("What is you name? ")

with open(filename, "w") as f:
    f.write(name)

# task 10-4 Guest Book
from datetime import datetime

filename = "guest_book.txt"

prompt = "What is you name?: "

is_guest_waiting = True

with open(filename, "a") as f:
    while is_guest_waiting:
        name = input(prompt)
        current_datetime = datetime.now().isoformat(" ", "seconds")
        print(f"Hello, {name}!")
        f.write(f"{current_datetime}\t{name}\n")

        repeat = input("Would anyone else like to sign the guestbook? (y/n) ")
        if repeat == "n":
            is_guest_waiting = False

# task 10-5 Programming Poll
filename = "pool.txt"
prompt = "What do you like about programming?"
prompt += "\nEnter 'q' to finished: "

with open(filename, "a") as f:
    while True:
        answer = input(prompt)

        if answer in ("q", "quit"):
            break
        else:
            f.write(f"{answer}\n")
