# task 8-1
def dispaly_message():
    print(
        "Docstrings."
        "\nThese are special comments that explain the purpose of functions, classes, or modules. "
        "\nThey can be accessed through the .__doc__ attribute."
    )


dispaly_message()


# task 8-2
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")


favorite_book("Bible")
