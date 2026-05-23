import unittest

from chapter_11.city import city_info


# task 11-1 City, Country
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formated_city_country = city_info("paris", "france")
        self.assertEqual(formated_city_country, "Paris France")

    def test_city_country_population(self):
        formated_city_country_population = city_info("paris", "france", 2200000)
        self.assertEqual(
            formated_city_country_population, "Paris France — population 2200000"
        )
