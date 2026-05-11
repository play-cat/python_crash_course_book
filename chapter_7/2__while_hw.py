# task 7-4 Pizza ingredients
prompt = "Enter the ingredient you want to add to the pizza."
prompt += "\n(Enter 'quit' when you are finished.)"

requested_ingredient = ""

while requested_ingredient != "quit":
    requested_ingredient = input(prompt)

    if requested_ingredient != "quit":
        print(f"\n{requested_ingredient} were added to the pizza.")

# task 7-5 Movie tickets
prompt = "How old are you?"
prompt += "\n(Enter 'quit' when you are finished.) "
age = ""

while age != "quit":
    age = input(prompt)
    ticket_price = 0

    if age != "quit":
        if int(age) < 3:
            print(f"\nTicket price ${ticket_price}")
        elif int(age) < 12:
            ticket_price = 10
            print(f"\nTicket price ${ticket_price}")
        else:
            ticket_price = 15
            print(f"\nTicket price ${ticket_price}")

# task 7-6
prompt = "Enter the ingredient you want to add to the pizza."
prompt += "\n(Enter 'quit' when you are finished.)"
requested_ingredient = ""

# v1
active = True

while active:
    requested_ingredient = input(prompt)
    if requested_ingredient == "quit":
        active = False

    print(f"\n{requested_ingredient} were added to the pizza.")

# v2
prompt = "\nEnter the ingredient you want to add to the pizza."
prompt += "\n(Enter 'quit' when you are finished.)"
requested_ingredient = ""

while True:
    requested_ingredient = input(prompt)
    if requested_ingredient == "quit":
        break
    else:
        print(f"\n{requested_ingredient} were added to the pizza.")

# task 7-7 endless loop
x = 1
while x < 5:
    print(x)
