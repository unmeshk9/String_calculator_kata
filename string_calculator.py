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
        return sum(int(n) for n in parts)
