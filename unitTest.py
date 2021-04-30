import calc
import unittest


class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(12, 22), 34)

    def test_add_2(self):
        self.assertEqual(calc.add(3, 7), 10)


class testCaseSubtract(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.subtract(12, 22), -10)

    def test_add_2(self):
        self.assertEqual(calc.subtract(3, 7), -4)


class testCaseMultiply(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.multiply(12, 22), 12*22)

    def test_add_2(self):
        self.assertEqual(calc.multiply(3, 7), 3*7)


class testCaseDivide(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.divide(12, 22), 12/22)

    def test_add_2(self):
        self.assertEqual(calc.divide(3, 7), 3/7)


if __name__ == '__main__':
    unittest.main()
