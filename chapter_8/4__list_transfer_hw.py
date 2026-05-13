# task 8-9 Message
messages = [
    "Debugging is my cardio.",
    "Code fast, test faster.",
    "Keep calm and commit.",
    "Python makes life easier.",
    "Shift happens, handle errors.",
]


def show_message(messages_list):
    for message in messages_list:
        print(message)


show_message(messages)

# task 8-10 Send message
sent_messages = []


def send_messages(messages_list):
    while messages_list:
        message = messages_list.pop()
        print(f"Sending a message: {message}")
        print("Message sent.")
        sent_messages.append(message)

    sent_messages.reverse()


send_messages(messages)

print(sent_messages)
print(messages)

# task 8-11 Archived messages
messages = [
    "Debugging is my cardio.",
    "Code fast, test faster.",
    "Keep calm and commit.",
    "Python makes life easier.",
    "Shift happens, handle errors.",
]
sent_messages = []

send_messages(messages[:])

print("\nSending messages:")
print(sent_messages)
print("Archived messages:")
print(messages)
