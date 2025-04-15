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
                # Multi-character delimiter
                end = numbers.index(']')
                delimiter = numbers[3:end]
                numbers = numbers[end+2:]
            else:
                delimiter = numbers[2]
                numbers = numbers[4:]
        # Replace newline with delimiter for consistent tokenization
        numbers = numbers.replace("\n", delimiter)
        parts = re.split(re.escape(delimiter), numbers)
        nums = [int(n) for n in parts if n]
        # Raise error if any negative numbers are found
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")
        # Ignore any number greater than 1000 per spec
        nums = [n for n in nums if n <= 1000]
        return sum(nums)
