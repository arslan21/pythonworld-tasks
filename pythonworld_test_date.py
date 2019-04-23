# проверка правильности даты
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def date(day, month, year):
    monthDays = {1: 31, 2: 29 if is_year_leap(year) else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    if month > 12:
        return False
    else:
        if day > monthDays[month]:
            return False
        else:
            return True

import unittest


class DateTestCase(unittest.TestCase):

    def test_leap_years(self):

        for year in (2000, 2016, 1916):
            with self.subTest(year=year):
                self.assertTrue(date(29, 2, year),
                                "{} високосный".format(year))

        for year in (1900, 2014, 2001):
            with self.subTest(year=year):
                self.assertFalse(date(29, 2, year),
                                 "{} не високосный".format(year))

    def test_valid_dates(self):

        self.assertTrue(date(1, 1, 1900))
        self.assertTrue(date(28, 2, 1900))
        self.assertTrue(date(1, 1, 1))
        self.assertTrue(date(31, 1, 2000))
        self.assertTrue(date(31, 12, 1900))

    def test_invalid_month(self):

        self.assertFalse(date(1, 13, 1900))
        self.assertFalse(date(2, 14, 2003))

    def test_invalid_day(self):

        self.assertFalse(date(32, 1, 1900))
        self.assertFalse(date(30, 2, 1900))
        self.assertFalse(date(31, 4, 1900))

    def test_invalid_all(self):

        self.assertFalse(date(32, 13, 1900))


if __name__ == "__main__":
    unittest.main()

