# указание сезона
def season(month):
    year = ('зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима')
    return year[month - 1]



import unittest


class SeasonTestCase(unittest.TestCase):

    def test_season(self):
        seasons = [None, 'зима', 'зима', 'весна', 'весна', 'весна',
                   'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

        for month in range(1, 13):
            with self.subTest(month=month):
                self.assertEqual(season(month).lower(), seasons[month])



if __name__ == "__main__":
    unittest.main()
