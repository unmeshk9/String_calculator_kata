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

    def test_newline_as_delimiter(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1\n2,3"), 6)
        self.assertEqual(calc.add("4\n5\n6"), 15)

    def test_custom_single_char_delimiter(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//;\n1;2"), 3)
        self.assertEqual(calc.add("//@\n2@3@4"), 9)

    def test_negative_numbers_raise_exception(self):
        calc = StringCalculator()
        with self.assertRaises(ValueError):
            calc.add("1,-2,3")
        with self.assertRaises(ValueError):
            calc.add("//;\n-1;2;3")

    def test_exception_message_shows_all_negatives(self):
        calc = StringCalculator()
        try:
            calc.add("1,-2,-3,4")
        except ValueError as e:
            self.assertIn("-2", str(e))
            self.assertIn("-3", str(e))

    def test_ignore_numbers_greater_than_1000(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("2,1001"), 2)
        self.assertEqual(calc.add("1000,1001,6"), 1006)

    def test_multi_char_custom_delimiter(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//[***]\n1***2***3"), 6)
        self.assertEqual(calc.add("//[abc]\n4abc5abc6"), 15)

if __name__ == "__main__":
    unittest.main()
