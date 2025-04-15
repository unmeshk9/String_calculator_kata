import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        calc = StringCalculator()
        self.assertEqual(calc.add(""), 0)

    def test_single_number_returns_itself(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("5"), 5)

    def test_two_numbers_returns_sum(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1,2"), 3)

    def test_arbitrary_number_of_values(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1,2,3,4"), 10)
        self.assertEqual(calc.add("10,20,30"), 60)

if __name__ == "__main__":
    unittest.main()
