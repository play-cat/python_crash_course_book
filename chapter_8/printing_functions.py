def print_models(unprinted, completed):
    """Transfer all elements from one list to another"""
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}")
        completed.append(current_design)

    if completed:
        show_completed(completed)
    else:
        print("No models were printed")


def show_completed(completed_models):
    """We show all finished models"""
    print(f"\nThe following models have been printed ({len(completed_models)} pcs.):")
    for model in completed_models:
        print(f"- {model}")
