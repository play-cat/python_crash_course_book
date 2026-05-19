class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nAbout the user {self.first_name}:")
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

    def greet_user(self):
        print(f"\nWelcome, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = Privileges()


class Privileges:
    DEFAULT_PRIVILEGES = {
        "add_post": "can add post",
        "delete_post": "can delete post",
        "ban_user": "can ban user",
    }

    def __init__(self):
        self.privileges = self.DEFAULT_PRIVILEGES.copy()

    def show_privileges(self):
        if self.privileges:
            print("\nThis user has the following administrator privileges:")
            for value in self.privileges.values():
                print(f"- {value.title()}")
