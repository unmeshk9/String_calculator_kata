class StringCalculator:
    def add(self, numbers: str) -> int:
        # Return 0 for empty input as per spec
        if numbers == "":
            return 0
        # Handle single number input
        # Parse custom delimiters if string starts with "//"
        import re
        delimiter = ","
        if numbers.startswith("//"):
            if numbers[2] == '[':
                # Multiple delimiters of any length
                import re
                delimiters = re.findall(r'\[(.*?)\]', numbers)
                rest = numbers.split('\n', 1)[1]
                # Build regex pattern for all delimiters
                pattern = '|'.join(map(re.escape, delimiters))
                parts = re.split(pattern, rest)
            else:
                delimiter = numbers[2]
                rest = numbers[4:]
                parts = re.split(re.escape(delimiter), rest.replace("\n", delimiter))
        else:
            # Default: comma and newline as delimiters
            parts = re.split(',|\n', numbers)
        nums = [int(n) for n in parts if n]
        # Raise error if any negative numbers are found
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")
        # Ignore any number greater than 1000 per spec
        nums = [n for n in nums if n <= 1000]
        return sum(nums)
