class StringCalculator:
    def add(self, numbers: str) -> int:
        """
        Adds numbers provided in a string, supporting custom delimiters and special rules.
        - Empty string returns 0
        - Single or multiple numbers separated by comma, newline, or custom delimiters
        - Custom delimiters: //delimiter\n or //[delim1][delim2]\n
        - Negative numbers raise ValueError listing all negatives
        - Numbers > 1000 are ignored
        """
        # Return 0 for empty input
        if numbers == "":
            return 0

        import re  # Use regex for delimiter parsing and splitting
        delimiter = ","  # Default delimiter

        # Check for custom delimiter syntax at the start
        if numbers.startswith("//"):
            if numbers[2] == '[':
                # Handle multiple delimiters of any length, e.g. //[***][%%]\n1***2%%3
                delimiters = re.findall(r'\[(.*?)\]', numbers)
                rest = numbers.split('\n', 1)[1]
                # Build regex pattern to match any of the delimiters
                pattern = '|'.join(map(re.escape, delimiters))
                parts = re.split(pattern, rest)
            else:
                # Handle single-character custom delimiter, e.g. //;\n1;2
                delimiter = numbers[2]
                rest = numbers[4:]
                # Replace newline with delimiter for consistent splitting
                parts = re.split(re.escape(delimiter), rest.replace("\n", delimiter))
        else:
            # Default: split on comma or newline
            parts = re.split(',|\n', numbers)

        # Convert all non-empty string parts to integers
        nums = [int(n) for n in parts if n]

        # Raise error if any negative numbers are found, listing all negatives
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

        # Ignore any number greater than 1000
        nums = [n for n in nums if n <= 1000]

        # Return the sum of all valid numbers
        return sum(nums)

if __name__ == "__main__":
    calc = StringCalculator()
    test_input = input("Enter numbers string: ")
    try:
        result = calc.add(test_input)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
