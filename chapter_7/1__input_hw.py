# task 7-1 Car rent
prompt = "What brand of car do you want to rent? "
request = input(prompt)

print(f"Let me see if I can find you a {request}.")

# task 7-2 Seats in the restaurant
number_of_seats = int(input("How many people do you want to reserve a table for? "))

if number_of_seats > 8:
    print(
        f"Sorry, it will take a while for us to find a table for {number_of_seats} people."
    )
else:
    print("Congratulations! Your table is ready.")

# task 7-3 A number that is a multiple of 10
number = int(input("Enter a number and I'll tell you if it's a multiple of 10. "))

if number % 10 == 0:
    print(f"A number {number} is a multiple of 10.")
else:
    print(f"A number {number} is not a multiple of 10.")
