# String Calculator TDD Kata (Incubyte Assessment)

This is my implementation of the **String Calculator Kata** using **Test-Driven Development (TDD)** in Python.

## Features Implemented

| Feature | Description |
|--------|-------------|
| Empty string | Returns 0 |
| One/Two numbers | Returns their sum |
| Unknown number of values | Supports arbitrary count |
| Newline as delimiter | Handles `\n` along with `,` |
| Custom single-char delimiter | Format: `//;\n1;2` |
| Negative numbers | Raises exception with all negatives |
| Ignore numbers >1000 | Skips those in the sum |
| Delimiters of any length | Format: `//[***]\n1***2***3` |
| Multiple delimiters | Format: `//[*][%]\n1*2%3` |
| Multi-char delimiters | Format: `//[**][%%]\n1**2%%3` |

---

## How to Run

### Run unit tests
```bash
python -m unittest discover
```

### Run manually from the terminal
You can run the calculator interactively:
```bash
python string_calculator.py
```
You will be prompted to enter a numbers string (e.g., `1,2,3` or `//[***]\n1***2***3`). The result or any error will be printed in the terminal.

