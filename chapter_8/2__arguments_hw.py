# task 8-3 t-shirt
def make_shirt(size, text):
    print(f"\nSelected T-shirt size {size}.")
    print(f"Slogan on the T-shirt: {text}.")


make_shirt("L", "I like Java Script")
make_shirt(size="M", text="PYTHON: I'm Lovin 'It")


# task 8-4 t-shirt l-size
def make_shirt(size="L", text="I love Python"):
    print(f"\nSelected T-shirt size {size}.")
    print(f"Slogan on the T-shirt: {text}.")


make_shirt()
make_shirt("M")
make_shirt("S", "I like Java Script")


# task 8-5 Cities
def describe_city(city, country="ukraine"):
    print(
        f"\n{city.title()} is in {country.upper() if country == "usa" else country.title()}."
    )


describe_city("kyiv")
describe_city("krakiv", "poland")
describe_city(city="new york", country="usa")
