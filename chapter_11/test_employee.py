import unittest

from chapter_11.employee import Employee


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        new_employee = ["John", "Doe", 52000]
        self.emp = Employee(*new_employee)

    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.annual_salary, 57000)

    def test_give_custom_raise(self):
        self.emp.give_raise(10000)
        self.assertEqual(self.emp.annual_salary, 62000)


if __name__ == "__main__":
    unittest.main()
