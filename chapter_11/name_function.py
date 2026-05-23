def get_formatted_name(first, last, middle=""):
    """Return a formatted name for a given first and last name."""
    if middle:
        return f"{first} {middle} {last}".title()
    else:
        return f"{first} {last}".title()
