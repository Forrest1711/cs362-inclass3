import calc
import unittest


class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(12, 22), 34)

    def test_add_2(self):
        self.assertEqual(calc.add(3.377, 6.623), 10)

    def test_add_3(self):
        self.assertEqual(calc.add("banana", 12), "Error")


class testCaseSubtract(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(calc.subtract(12, 22), -10)

    def test_subtract_2(self):
        self.assertEqual(calc.subtract(3.3, 7.3), -4)

    def test_subtract_3(self):
        self.assertEqual(calc.subtract("apple", 11), "Error")


class testCaseMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(calc.multiply(12, 22), 12*22)

    def test_multiply_2(self):
        self.assertEqual(calc.multiply(3.88, 7.22), 3.88*7.22)

    def test_multiply_3(self):
        self.assertEqual(calc.multiply("orange", 67), "Error")


class testCaseDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(calc.divide(12, 22), 12/22)

    def test_divide_2(self):
        self.assertEqual(calc.divide(32.16, 7.73), 32.16/7.73)

    def test_divide_3(self):
        self.assertEqual(calc.divide("kiwi", 69), "Error")


if __name__ == '__main__':
    unittest.main()
