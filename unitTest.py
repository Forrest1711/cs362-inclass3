import calc
import unittest


class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(12, 22), 34)

    def test_add_2(self):
        self.assertEqual(calc.add(3, 7), 21)


if __name__ == '__main__':
    unittest.main()
