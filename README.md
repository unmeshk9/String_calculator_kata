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

#### Usage Steps
1. When prompted, enter your numbers string according to the supported formats below. Do **not** use quotes around your input.
2. For multi-line input (e.g., custom delimiters), type the first line, press Enter, then type the numbers line, and press Enter again.
3. The result or any error will be printed in the terminal.

#### Examples
- **Empty input:**
  - Just press Enter
  - Output: `Result: 0`

- **Single number:**
  - Input: `1`
  - Output: `Result: 1`

- **Comma-separated numbers:**
  - Input: `1,2,3`
  - Output: `Result: 6`

- **Newline as delimiter:**
  - Input:
    ```
    1
    2,3
    ```
  - Output: `Result: 6`

- **Custom single-character delimiter:**
  - Input:
    ```
    //;
    1;2
    ```
  - Output: `Result: 3`

- **Multiple delimiters:**
  - Input:
    ```
    //[*][%]
    1*2%3
    ```
  - Output: `Result: 6`

- **Multi-character delimiters:**
  - Input:
    ```
    //[***][%%]
    1***2%%3
    ```
  - Output: `Result: 6`

- **Negative numbers:**
  - Input: `1,-2,-3`
  - Output: `Error: Negatives not allowed: [-2, -3]`

- **Numbers > 1000 are ignored:**
  - Input: `2,1001`
  - Output: `Result: 2`

If you copy-paste a multi-line example, make sure your terminal supports multi-line input, or type each line and press Enter.
