from business_rules import(
    calculate_job_total,
    calculate_print_cost,
    get_volume_discount,
    largest_job,
    needs_overnight_run,
    requires_proof,
    total_invoiced
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

def test_overnight_at_limits():
    assert needs_overnight_run(500, 400) is False

def test_overnight_above_copies():
    assert needs_overnight_run(501, 400) is True

def test_overnight_above_total():
    assert needs_overnight_run(500, 400.01) is True

def test_overnight_below_limits():
    assert needs_overnight_run(499, 399) is False

def test_total_invoiced_two_jobs():
    jobs = [
        {"title": "Flyers", "copy_price": 0.25, "copies": 100},
        {"title": "Menus", "copy_price": 0.50, "copies": 150},
    ]
    assert round(total_invoiced(jobs), 2) == 115.00

def test_total_invoiced_empty():
    assert total_invoiced([]) == 0.0

def test_largest_job_one():
    jobs = [
        {"title": "Flyers", "copy_price": 0.25, "copies": 100}
    ]
    assert largest_job(jobs) == "Flyers"

def test_largest_job_different_totals():
    jobs = [
        {"title": "Flyers", "copy_price": 0.25, "copies": 100},
        {"title": "Menus", "copy_price": 0.50, "copies": 150},
    ]
    assert largest_job(jobs) == "Menus"

def test_largest_job_tie():
    jobs = [
        {"title": "Flyers", "copy_price": 0.50, "copies": 150},
        {"title": "Menus", "copy_price": 0.50, "copies": 150},
    ]
    assert largest_job(jobs) == "Flyers"

def test_largest_job_empty():
    assert largest_job([]) == ""

def test_format_line_no():
    assert format_job_line("Flyers", 25.0, False, False) == (
        "Flyers: $25.00 | proof: no | overnight run: no"
    )

def test_format_line_yes():
    assert format_job_line("Menus", 75.0, True, True) == (
        "Menus: $75.00 | proof: yes | overnight run: yes"
    )

