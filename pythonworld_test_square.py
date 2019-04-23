# расчет площади, периметра и диаганали по стороне квадрата
import math

def square(a):
    per = a * 4
    sq = math.pow(a, 2)
    dia = math.hypot(a, a)
    return(per, sq, dia)

import unittest


class SquareTestCase(unittest.TestCase):

    def test_square(self):

        for a in range(10):
            with self.subTest(a=a):
                self.assertCountEqual(
                    # Избегаем проблемы с числами с плавающей точкой
                    list(map(lambda x: round(x, 7), square(a))),
                    list(map(lambda x: round(x, 7), [4*a, a**2, a*math.sqrt(2)]))
                )



if __name__ == "__main__":
    unittest.main()
