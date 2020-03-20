# from city_functions import get_formatted_name
#
# print("If you enter 'q' at any time quit this program. ")
#
# while True:
#     city = input("Enter your favorite city: ")
#     if city == 'q':
#         break
#
#     country = input("Enter your favorite city located in: ")
#     if country == 'q':
#         break
#
#     formatted_name = get_formatted_name(city, country)
#     print(formatted_name)

##---------------------------------------------------------------------------------------------------------------------

import unittest
from city_functions import get_formatted_name

class TestCityName(unittest.TestCase):
    def test_city_country(self):
        formatted_name = get_formatted_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago Chile')

    def test_city_country_population(self):
        formatted_name = get_formatted_name('santiago', 'chile', 'population=5000000')
        self.assertEqual(formatted_name, 'Santiago Chile Population=5000000')

unittest.main()