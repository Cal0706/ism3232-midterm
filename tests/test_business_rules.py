from business_rules import(
    calculate_print_cost,
    get_volume_discount
)

def test_print_cost():
    assert calculate_print_cost(0.25, 100) == 25.0


def test_discount_below_200():
    assert get_volume_discount(199) == 0.0


def test_discount_at_200():
    assert get_volume_discount(200) == 0.08

