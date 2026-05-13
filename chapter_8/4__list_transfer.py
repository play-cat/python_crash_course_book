def greet_users(names):
    """Display a simple message for each user in the list"""
    for name in names:
        print(f"Hello, {name.title()}!")


usernames = ["alex", "hunchback", "margot"]
greet_users(usernames)

# edit list inside function
unprinted_design = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []


def print_models(unprinted, completed):
    """Transfer all elements from one list to another"""
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}")
        completed.append(current_design)


def show_completed(completed_models):
    """We show all finished models"""
    print(f"\nThe following models have been printed ({len(completed_models)} pcs.):")
    for model in completed_models:
        print(model)


print_models(unprinted_design, completed_models)
show_completed(completed_models)

# Як не дозволити функції видозмінити список
unprinted_design = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# Передаємо в функцію копію списку [:]
print_models(unprinted_design[:], completed_models)
show_completed(completed_models)

print(unprinted_design)
print(completed_models)
