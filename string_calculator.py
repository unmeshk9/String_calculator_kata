class StringCalculator:
    def add(self, numbers: str) -> int:
        # Return 0 for empty input as per spec
        if numbers == "":
            return 0
        # Handle single number input
        if "," in numbers:
            parts = numbers.split(",")
            return sum(int(n) for n in parts)
        return int(numbers)
