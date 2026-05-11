# Moving items from one list to another
unconfirmed_users = ["alice", "brian", "mark"]
confirmed_users = []

# Перебирати всіх користувачів з непідтвердженого списку
# і переносити в список підтверджених користувачів
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("The following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

# Як прибрати всі зустрічі певного значення зі списку
pets = ["dog", "cat", "bird", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)

# Як наповнити словник даними користувацького вводу
responses = {}

# булева зміна показує що опитування в процесі
polling_active = True

while polling_active:
    # спитати ім'я
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # зберегти відповідь у словник
    responses[name] = response

    # спитати чи ще хтось хоче проходити опитування
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n----- Pool results -----")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")
