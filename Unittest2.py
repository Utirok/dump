import random
import unittest
import numpy as numpy


class Main(unittest.TestCase):
    def test_random(self):
        fractions = numpy.random.random(50)
        print(fractions)
        for fraction in fractions:
            with self.subTest(x=fraction):
                self.assertGreaterEqual(fraction, 0.5)


if __name__ == '__main__':
    unittest.main()
