Blueprint.md — TDD String Calculator Kata (Incubyte Assignment)
This blueprint guides you through implementing the String Calculator Kata using TDD, with exact GitHub commit moments, messages, and code comments. Built for craftsmanship.

🛠 Initial Setup
1. 🏁 Initialize project
bash
mkdir string_calculator && cd string_calculator
git init
touch string_calculator.py test_string_calculator.py README.md
2. 🧪 Add test scaffold
Use Python’s unittest.

python
# test_string_calculator.py
import unittest
from string_calculator import StringCalculator
✅ Git Commit
bash
git add .
git commit -m "Setup project scaffolding and testing framework"
✅ TDD Steps + Commits
🧪 Step 1: Empty string → 0
Test: "" → 0

Code: Return 0 for empty input

python
# string_calculator.py
class StringCalculator:
    def add(self, numbers: str) -> int:
        # Return 0 for empty input as per spec
        return 0
bash
git commit -am "Handle empty string: return 0"
🧪 Step 2: Single number returns itself
bash
git commit -am "Handle single number input"
🧪 Step 3: Two numbers → sum
bash
git commit -am "Add support for two comma-separated numbers"
🧪 Step 4: Arbitrary number of values
bash
git commit -am "Support unknown amount of comma-separated numbers"
🧪 Step 5: Newline (\n) as delimiter
bash
git commit -am "Allow newline character as a valid delimiter"
🧪 Step 6: Custom single-char delimiter (e.g. "//;\n1;2")
Parse custom delimiter from prefix

Use re.split() for flexibility

bash
git commit -am "Support single-character custom delimiters"
🧪 Step 7: Negative numbers → raise exception
bash
git commit -am "Raise exception for negative numbers"
🧪 Step 8: Show all negatives in exception message
bash
git commit -am "Show all negatives in exception error message"
🧪 Step 9: Ignore numbers > 1000
bash
git commit -am "Ignore numbers greater than 1000"
🧪 Step 10: Delimiters of any length (e.g., "//[***]\n")
bash
git commit -am "Support multi-character custom delimiters"
🧪 Step 11: Multiple delimiters ("//[*][%]\n1*2%3")
bash
git commit -am "Add support for multiple delimiters"
🧪 Step 12: Multi-char multiple delimiters ("//[**][%%]\n")
bash
git commit -am "Add support for multi-character multiple delimiters"
📦 Finalization
✅ Create README.md
Document:

How to run tests

Features covered

Screenshot instructions

bash
git add README.md
git commit -m "Add README with instructions and feature checklist"
📸 Take Screenshot
Run tests:

bash
python -m unittest discover
Take a screenshot of green tests and add it to screenshots/all_tests_passing.png.

bash
git add screenshots/all_tests_passing.png
git commit -m "📸 Add test results screenshot"
📤 Push to GitHub
bash
gh repo create string-calculator-tdd --public --source=. --remote=origin
git push -u origin main
🧼 Code Comment Best Practices
In string_calculator.py, add comments like:

python
# Parse custom delimiters if string starts with "//"
# Replace newline with delimiter for consistent tokenization
# Raise error if any negative numbers are found
# Ignore any number greater than 1000 per spec
✅ Final Commit Message
bash
git commit --allow-empty -m "Complete TDD String Calculator Kata with clean tests and documentation"
🏁 Done!
Your submission will now reflect:

🔁 Thoughtful TDD progression

🧪 Full coverage of specs

✅ Polished README

🧼 Clean, commented code

📸 Screenshot proof

📚 Git history that shows craftsmanship