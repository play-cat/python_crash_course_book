import unittest

from chapter_11.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        formated_name = get_formatted_name("bobby", "dilan")
        self.assertEqual(formated_name, "Bobby Dilan")

    def test_first_last_middle_name(self):
        formated_name = get_formatted_name("wolf", "mozart", "amadeus")
        self.assertEqual(formated_name, "Wolf Amadeus Mozart")


if __name__ == "__main__":
    unittest.main()
