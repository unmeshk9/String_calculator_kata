import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        calc = StringCalculator()
        self.assertEqual(calc.add(""), 0)

    def test_single_number(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("5"), 5)

    def test_two_numbers(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1,2"), 3)

    def test_any_number_of_values(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1,2,3,4"), 10)
        self.assertEqual(calc.add("10,20,30"), 60)

    def test_newline_delimiter(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1\n2,3"), 6)
        self.assertEqual(calc.add("4\n5\n6"), 15)

    def test_custom_single_char_delim(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//;\n1;2"), 3)
        self.assertEqual(calc.add("//@\n2@3@4"), 9)

    def test_negatives_raise(self):
        calc = StringCalculator()
        with self.assertRaises(ValueError):
            calc.add("1,-2,3")
        with self.assertRaises(ValueError):
            calc.add("//;\n-1;2;3")

    def test_negatives_in_message(self):
        calc = StringCalculator()
        try:
            calc.add("1,-2,-3,4")
        except ValueError as e:
            self.assertIn("-2", str(e))
            self.assertIn("-3", str(e))

    def test_ignore_big_numbers(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("2,1001"), 2)
        self.assertEqual(calc.add("1000,1001,6"), 1006)

    def test_multi_char_delim(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//[***]\n1***2***3"), 6)
        self.assertEqual(calc.add("//[abc]\n4abc5abc6"), 15)

    def test_multiple_delims(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//[*][%]\n1*2%3"), 6)
        self.assertEqual(calc.add("//[@][#]\n4@5#6"), 15)

    def test_multi_char_multiple_delimiters(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//[**][%%]\n1**2%%3"), 6)
        self.assertEqual(calc.add("//[ab][cd]\n4ab5cd6"), 15)

if __name__ == "__main__":
    unittest.main()
