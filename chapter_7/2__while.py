# while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program: "
message = ""

while message not in ("quit", "exit"):
    message = input(prompt)
    if message not in ("quit", "exit"):
        print(message)

# true/false
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

# break
prompt = "\nPlease enter the name of city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# continue
current_number = 0
while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

    print(current_number)
