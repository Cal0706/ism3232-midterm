def calculate_print_cost(price_per_copy, copies):
    return price_per_copy * copies


def calculate_discount(copies):
    if copies >= 1000:
        return 0.15
    elif copies >= 200:
        return 0.08
    else:
        return 0.0


def calculate_student_discount(copies, is_student_org):
    discount = calculate_discount(copies)

    if is_student_org and copies >= 200:
        discount += 0.05

    return discount


print(calculate_student_discount(100, True))
print(calculate_student_discount(500, True))
print(calculate_student_discount(1200, True))
print(calculate_student_discount(500, False))



