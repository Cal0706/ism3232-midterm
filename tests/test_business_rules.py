from business_rules import(
    calculate_job_total,
    calculate_print_cost,
    get_volume_discount,
    requires_proof
)

def test_print_cost_100_copies():
    assert calculate_print_cost(0.25, 100) == 25.0

def test_print_cost_200_copies():
    assert calculate_print_cost(0.50, 200) == 100.0

def test_discount_below_200():
    assert get_volume_discount(199) == 0.0

def test_discount_at_200():
    assert get_volume_discount(200) == 0.08

def test_discount_above_200():
    assert get_volume_discount(250) == 0.08

def test_discount_999():
    assert get_volume_discount(999) == 0.08

def test_discount_1000():
    assert get_volume_discount(1000) == 0.15

def test_student_discount_200():
    assert get_volume_discount(200, True) == 0.13

def test_student_discount_1000():
    assert get_volume_discount(1000, True) == 0.20

def test_job_total_setup_fee():
    assert round(calculate_job_total(0.25, 100), 2) == 40.00

def test_job_total_no_fee():
    assert round(calculate_job_total(0.50, 150), 2) == 75.00

def test_job_total_with_discount():
    assert round(calculate_job_total(0.10, 200), 2) == 33.40

def test_proof_at_300():
    assert requires_proof(300.00) is False

def test_proof_above_300():
    assert requires_proof(300.01) is True
