class StringCalculator:
    def add(self, numbers: str) -> int:
        # Return 0 for empty input as per spec
        if numbers == "":
            return 0
        # Handle single number input
        # Parse custom delimiters if string starts with "//"
        delimiter = ","
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]  # skip // and delimiter and newline
        numbers = numbers.replace("\n", delimiter)
        parts = numbers.split(delimiter)
        nums = [int(n) for n in parts]
        # Raise error if any negative numbers are found
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")
        # Ignore any number greater than 1000 per spec
        nums = [n for n in nums if n <= 1000]
        return sum(nums)
