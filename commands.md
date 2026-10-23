# Terminal Record: Brightline Print Shop

## 1. Building the project
Creating the project folder = mkdir ism3232-midterm
Enter project folder = cd ism3232-midterm
Create virtual environment = python3 -m venv .venv
Activate environment = source .venv/bin/activate
Create Python files = touch business_rules.py main.py
Create other files = touch README.md requirements.txt .gitignore
Create tests folder = mkdir tests
Create test files = touch tests/__init__.py tests/test_business_rules.py
Initialize Git = git init
Connect GitHub = git remote add origin https://github.com/Cal0706/ism3232-midterm.git
## 2. The virtual environment
```bash
which python3
```
```text
/Users/camlopez/Desktop/ism3232-midterm/.venv/bin/python3
```
The output shows that the virtual environment is active because this is located inside the project's .venv/bin directory.
## 3. The project structure
```bash
tree -L 2
```
```test
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
```
One of the folders that is present in the output but is not in my GutHub repository is the __pycache__ folder. It is not included because it contains automatically generated Python cache files that are excludede in .gitignore and don't need to be uploaded.
## 4. Every function and test
```bash
rg 'def ' business_rules.py tests/test_business_rules.py
```
```text
business_rules.py
1:def calculate_print_cost(copy_price: float, copies: int) -> float:
6:def get_volume_discount(copies: int, student_org: bool = False) -> float:
21:def calculate_job_total():
36:def requires_proof(total: float) -> bool:
41:def needs_overnight_run(copies: int, total: float) -> bool:
46:def total_invoiced(jobs: list) -> float:
59:def largest_job(jobs: list) -> str:
76:def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:

tests/test_business_rules.py
13:def test_print_cost_100_copies():
17:def test_print_cost_200_copies():
21:def test_discount_below_200():
25:def test_discount_at_200():
29:def test_discount_above_200():
33:def test_discount_999():
37:def test_discount_1000():
41:def test_student_discount_200():
45:def test_student_discount_1000():
49:def test_job_total_setup_fee():
53:def test_job_total_no_fee():
57:def test_job_total_with_discount():
61:def test_proof_at_300():
65:def test_proof_above_300():
69:def test_overnight_at_limits():
73:def test_overnight_above_copies():
77:def test_overnight_above_total():
81:def test_overnight_below_limits():
85:def test_total_invoiced_two_jobs():
93:def test_total_invoiced_empty():
97:def test_largest_job_one():
102:def test_largest_job_different_totals():
110:def test_largest_job_tie():
118:def test_largest_job_empty():
122:def test_format_line_no():
128:def test_format_line_yes():
```
The commands output from business_rules has 8 functions defined and tests/test_business_rules.py has 26 tests defined.
## 5. Which files print
```bash
rg -l 'print'
```
```text
README.md
commands.md
business_rules.py
main.py
tests/test_business_rules.py
```
The README.md, commmands.md, business_rules.py, main.py, and tests/test_business_rules.py files print after the command. The business_rules.py only prints because the command asks for every time the word 'print' is included in function names, variables and descriptions, even though there are no print statements.
## 6. The commit history
```bash
git log --oneline
```
```text
07aa6b6 (HEAD -> main, origin/main) Working on the commands.md and testing each command
2dd7bb7 Finished all 26 tests of the business rules
deb2759 About half way through the testing of the business rules
867724b Start the testing of the business rules
0fd78db Add main.py to generate print shop job report
425251f Add print shop project files and information
adfd8f2 Implement print cost and discount rules
```
At this point there were 7 commits from part 1 - 4.