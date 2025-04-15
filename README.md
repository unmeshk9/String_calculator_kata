# String Calculator Kata (Incubyte Assignment)

This project implements the String Calculator Kata using Test-Driven Development (TDD), following clean code and commit craftsmanship.

## How to run tests

```bash
python -m unittest discover
```

## Features covered
- Empty string returns 0
- Single number returns itself
- Two numbers, comma-delimited, returns sum
- Arbitrary number of values
- Newline (\n) as delimiter
- Custom single-character delimiter (e.g., //;\n1;2)
- Negative numbers raise exception (with all negatives in message)
- Ignore numbers > 1000
- Delimiters of any length (e.g., //[***]\n1***2)
- Multiple delimiters (e.g., //[*][%]\n1*2%3)
- Multiple multi-character delimiters (e.g., //[**][%%]\n1**2%%3)

## Screenshot instructions
1. Run all tests:
   ```bash
   python -m unittest discover
   ```
2. Take a screenshot of the terminal showing all tests passing.
3. Save it as `screenshots/all_tests_passing.png` (create the `screenshots` folder if it doesn't exist).
4. Add and commit:
   ```bash
   git add screenshots/all_tests_passing.png
   git commit -m "📸 Add test results screenshot"
   ```

## How to push to GitHub
If you haven't already, create a GitHub repo and push:
```bash
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

---
Happy Coding!
