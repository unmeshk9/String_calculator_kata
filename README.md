# String Calculator

This is a simple string calculator written in Python. It can add numbers from a string, using commas, newlines, or custom delimiters. I wrote this to practice clean coding and TDD.

## What it does
- Returns 0 for an empty string
- Adds up numbers separated by commas (e.g. `1,2,3` → 6)
- Handles newlines as delimiters (e.g. `1\n2,3` → 6)
- Lets you specify a custom delimiter (e.g. `//;\n1;2` → 3)
- Supports multiple or multi-character delimiters (e.g. `//[*][%]\n1*2%3`)
- Throws an error if there are negative numbers, listing all of them
- Ignores numbers greater than 1000

## How to use it

### Run the tests
```bash
python -m unittest discover
```

### Try it out yourself
```bash
python string_calculator.py
```
You'll see:
```
Enter numbers string:
```
Type your input (see below for examples) and press Enter. For multi-line input (like custom delimiters), type the first line, press Enter, then type the next line and press Enter.

### Examples
- Just press Enter: `Result: 0`
- `1,2,3` → `Result: 6`
- `1\n2,3` (type 1, press Enter, then 2,3, then Enter) → `Result: 6`
- Custom delimiter:
  ```
  //;
  1;2
  ```
  Output: `Result: 3`
- Multiple delimiters:
  ```
  //[*][%]
  1*2%3
  ```
  Output: `Result: 6`
- Multi-character delimiters:
  ```
  //[***][%%]
  1***2%%3
  ```
  Output: `Result: 6`
- Negative numbers (e.g. `1,-2,-3`) → `Error: Negatives not allowed: [-2, -3]`
- Numbers >1000 (e.g. `2,1001`) → `Result: 2`

If you paste a multi-line example, make sure your terminal supports it, or just type each line and press Enter.

---

If you have any questions or spot a bug, feel free to reach out!
