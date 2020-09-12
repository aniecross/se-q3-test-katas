import unittest
import katas
import math


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(5, 5), 10)

    def test_multiply(self):
        self.assertEqual(katas.multiply(5, 2), 10)

    def test_power(self):
        self.assertEqual(katas.power(5, 2), math.pow(5, 2))

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), math.factorial(5))

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(8), 21)


if __name__ == '__main__':
    unittest.main()
