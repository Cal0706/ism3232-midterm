# ISM3232 Midterm: Brightline Print Shop

- **Name:** Cam Lopez
- **Version:** GAMMA
- **Date:** 10/23/26

## What This Program Does
This program determines each print job price by the copy and invoices of the customer. It determines what kind of discount should be applied based on amount of copies and whether or not the customer is a registereed student organization. And it determines whether a print job needs a printed proof or an overnight press run.

## Business Rules
The print cost is the price per copy times the number of copies. The discount depends on the number of copies: < 200 copies = No discount, 200 - 900 copies = 8% discount, > 1000 copies = 15% discount. Registered student organizations get an extra 5% of discount, but only on jobs of 200 copies or more. For them, 8% becomes 13% and 15% becomes 20%. A $15 setup fee is added when the discounted cost is below $40. A job total of more than $300 requires a printed proof. A job needs an overnight press run when it has more than 500 copies or its job total is over $400.

## How to Run
Open the project folder in the terminal and run:
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```
## How to Test
Run these commands to check the code and run the tests:
```bash
ruff check .
pytest -v
```
## Files in This Repository
business_rules.py - Has all eight function for calculating printing prices and job requirements.
main.py - Runs the program and shows the report.
commands.md - Shows each terminal command used for the project.
README.md - Explains how to use and test the program.
requirements.txt - Shows the Pyton packages needed.
.gitignore - Prevents unnecessary files from being uploaded.
tests/__init__.py - Shows the tests folder as a Python package.
tests/test_business_rules.py - Has the automated tests.

## AI Use Statement
I did not use AI for this midterm.
