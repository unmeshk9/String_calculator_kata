class StringCalculator:
    def add(self, numbers: str) -> int:
        """
        Adds up numbers in a string. Handles commas, newlines, and custom delimiters.
        Returns 0 for empty input. Throws an error if there are negatives (shows all of them). Ignores numbers >1000.
        """
        if numbers == "":
            return 0

        import re
        delimiter = ","

        # Check for custom delimiter at the start
        if numbers.startswith("//"):
            if numbers[2] == '[':
                # Multiple delimiters, possibly multi-char
                delimiters = re.findall(r'\[(.*?)\]', numbers)
                rest = numbers.split('\n', 1)[1]
                pattern = '|'.join(map(re.escape, delimiters))
                parts = re.split(pattern, rest)
            else:
                # Single-char custom delimiter
                delimiter = numbers[2]
                rest = numbers[4:]
                parts = re.split(re.escape(delimiter), rest.replace("\n", delimiter))
        else:
            # Default: comma or newline
            parts = re.split(',|\n', numbers)

        nums = [int(n) for n in parts if n]

        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

        nums = [n for n in nums if n <= 1000]
        return sum(nums)

if __name__ == "__main__":
    calc = StringCalculator()
    test_input = input("Enter numbers string: ")
    try:
        result = calc.add(test_input)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
