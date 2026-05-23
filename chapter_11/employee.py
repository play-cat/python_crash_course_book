class Employee:
    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = int(annual_salary)

    def give_raise(self, amount=5000):
        self.annual_salary += amount

    def show_salary(self):
        print(self.annual_salary)
