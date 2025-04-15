import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        calc = StringCalculator()
        self.assertEqual(calc.add(""), 0)

    def test_single_number_returns_itself(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("5"), 5)

if __name__ == "__main__":
    unittest.main()
